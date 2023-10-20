/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect, useCallback, useRef } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import MapGL, { useControl } from 'react-map-gl/maplibre';
import MapboxDraw from '@mapbox/mapbox-gl-draw';
import * as MapboxDrawGeodesic from 'mapbox-gl-draw-geodesic';
import maplibregl from 'maplibre-gl';
// 其他第三方辅助
import { useRequest } from 'ahooks';
import bbox from '@turf/bbox';
import circle from '@turf/circle';
import intersects from '@turf/boolean-intersects';
import contains from '@turf/boolean-contains';
import length from '@turf/length';
import area from '@turf/area';
import omitBy from 'lodash/omitBy';
// 依赖库相关样式
import 'maplibre-gl/dist/maplibre-gl.css';
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css';
// 自定义样式
import '../css/base.css';

// 修复mapbox-gl-draw工具按钮显示异常问题
MapboxDraw.constants.classes.CONTROL_BASE = "maplibregl-ctrl";
MapboxDraw.constants.classes.CONTROL_PREFIX = "maplibregl-ctrl-";
MapboxDraw.constants.classes.CONTROL_GROUP = "maplibregl-ctrl-group";

// 额外绘图模式注册
let _modes = MapboxDraw.modes;
_modes = MapboxDrawGeodesic.enable(_modes);
_modes.static = void 0;
delete _modes.static;

// 定义部分exact型prop的默认值
const defaultExactProps = {
    drawControls: {
        point: true,
        line_string: true,
        polygon: true,
        draw_circle: true,
        trash: true,
        combine_features: false,
        uncombine_features: false,
    },
};

// 定义文案信息默认值
const defaultLocaleInfo = {
    'zh-cn': {
        'NavigationControl.ZoomIn': '放大地图',
        'NavigationControl.ZoomOut': '缩小地图',
        'NavigationControl.ResetBearing': '重置地图角度',
        'DrawControl.LineStringTool': '绘制线',
        'DrawControl.PolygonTool': '绘制面',
        'DrawControl.MarkerTool': '绘制点',
        'DrawControl.Delete': '删除',
        'DrawControl.Combine': '组合',
        'DrawControl.Uncombine': '取消组合',
    },
    'en-us': {
        'NavigationControl.ZoomIn': 'Zoom in',
        'NavigationControl.ZoomOut': 'Zoom out',
        'NavigationControl.ResetBearing': 'Reset bearing',
        'DrawControl.LineStringTool': 'Draw linestring',
        'DrawControl.PolygonTool': 'Draw polygon',
        'DrawControl.MarkerTool': 'Draw marker',
        'DrawControl.Delete': 'Delete',
        'DrawControl.Combine': 'Combine',
        'DrawControl.Uncombine': 'Uncombine',
    }
}

const DrawControl = (props) => {
    let drawRef = useRef(null);
    const {
        position,
        locale,
        localeInfo,
        drawOnlyOne,
        drawCircleSteps,
        enableDrawSpatialJudge,
        drawSpatialJudgePredicate,
        drawSpatialJudgeListenLayerIds,
        drawDeleteAll,
        drawDeleteSelected,
        setDrawMode,
        setProps,
        mapRef
    } = props;

    const onUpdate = useCallback((e) => {

        // 提取最新绘制的面要素
        let _drawnFeatures = drawRef.getAll().features;
        let latestDrawnFeature = _drawnFeatures[_drawnFeatures.length - 1];
        // 处理圆形要素
        if (latestDrawnFeature.properties.circleRadius) {
            latestDrawnFeature = circle(
                latestDrawnFeature.geometry.coordinates[0][0],
                latestDrawnFeature.properties.circleRadius,
                { steps: drawCircleSteps })
        }
        // 若最近绘制的要素类型为多边形
        if (enableDrawSpatialJudge && drawSpatialJudgeListenLayerIds.length > 0 && latestDrawnFeature.geometry.type === 'Polygon') {
            // 则计算求得与之相交的其他要素
            // 取得绘制面要素的box范围
            let polygonBoundingBox = bbox(latestDrawnFeature);
            // 计算box对应关键坐标
            let southWest = [polygonBoundingBox[0], polygonBoundingBox[1]];
            let northEast = [polygonBoundingBox[2], polygonBoundingBox[3]];

            // 计算对应的再投影空间范围
            let northEastPointPixel = mapRef.current.project(northEast);
            let southWestPointPixel = mapRef.current.project(southWest);

            // 基于地图像素范围的粗略查询过滤
            let roughMatchFeatures = mapRef.current.queryRenderedFeatures(
                [southWestPointPixel, northEastPointPixel],
                { layers: drawSpatialJudgeListenLayerIds }
            );

            // 基于相交关系运算保留实际发生相交的图层要素
            roughMatchFeatures = roughMatchFeatures.filter(
                // 根据drawSpatialJudgePredicate对应的拓扑关系类型进行判断
                (feature) => {
                    try {
                        return drawSpatialJudgePredicate === 'intersects' ?
                            intersects(latestDrawnFeature, feature) :
                            contains(latestDrawnFeature, feature);
                    } catch (e) {
                        // TEMP
                        // 针对多部件线要素等特殊的turf.contains()拓扑判断不支持问题进行暂时忽略
                        return false;
                    }
                }
            )

            setProps({
                // 更新与已绘制矢量实际发生相交的图层要素信息
                drawSpatialJudgeListenLayerFeatures: roughMatchFeatures.map((e) => {
                    return {
                        layer: {
                            id: e.layer.id,
                            source: e.layer.source,
                            sourceLayer: e.layer['source-layer'],
                            type: e.layer.type,
                        },
                        properties: e.properties,
                        source: e.properties,
                        sourceLayer: e.sourceLayer,
                        type: e.type,
                        _geometry: e._geometry
                    };
                }),
            });
        } else {
            setProps({
                // 其他情况下，重置为[]
                drawSpatialJudgeListenLayerFeatures: [],
            });
        }

        // 更新最新的已绘制要素数组到drawnFeatures中
        setProps({
            drawnFeatures: drawRef.getAll().features.map(
                g => {
                    // 若当前元素为线要素
                    if (g.geometry.type.toLowerCase().includes('line')) {
                        // 单位：千米
                        g.length = length(g, { units: 'kilometers' })
                    } else if (g.properties.circleRadius) {
                        // 单位：平方米
                        g.circle = circle(g.geometry.coordinates[0][0], g.properties.circleRadius, { steps: drawCircleSteps })
                        g.area = area(g.circle)
                    } else if (g.geometry.type.toLowerCase().includes('polygon')) {
                        // 单位：平方米
                        g.area = area(g)
                    }
                    return g;
                }
            )
        })
    }, [drawCircleSteps]);

    const onDelete = useCallback((e) => {
        // 更新最新剩余的已绘制要素数组到drawnFeatures中
        setProps({
            drawnFeatures: drawRef.getAll().features.map(
                g => {
                    // 若当前元素为线要素
                    if (g.geometry.type.toLowerCase().includes('line')) {
                        // 单位：千米
                        g.length = length(g, { units: 'kilometers' })
                    } else if (g.properties.circleRadius) {
                        // 单位：平方米
                        g.circle = circle(g.geometry.coordinates[0][0], g.properties.circleRadius, { steps: drawCircleSteps })
                        g.area = area(g.circle)
                    } else if (g.geometry.type.toLowerCase().includes('polygon')) {
                        // 单位：平方米
                        g.area = area(g)
                    }
                    return g;
                }
            )
        })
    }, [drawCircleSteps]);

    const onModeChange = useCallback(
        (e) => {
            if (
                ['draw_polygon', 'draw_line_string', 'draw_point'].includes(
                    e.mode
                )
            ) {
                // 取得当前全部图层的id并仅保留gl-draw*相关图层
                let allDrawLayerIds = mapRef.current.getStyle().layers.map(layer => layer.id).filter(layerId => layerId.startsWith('gl-draw'));
                // 针对相关图层按照原始顺序调整图层至顶层
                allDrawLayerIds.forEach(layerId => mapRef.current.moveLayer(layerId))
                if (drawOnlyOne) {
                    // 开始新的要素绘制之前清除先前已绘制要素
                    let _drawnFeatures = drawRef.getAll().features;
                    if (enableDrawSpatialJudge) {
                        setProps({
                            // 在新矢量开始绘制时，重置为[]
                            drawSpatialJudgeListenLayerFeatures: [],
                        });
                    }
                    // 取得最新添加的要素的id
                    let latestDrawnFeatureId = _drawnFeatures[_drawnFeatures.length - 1].id;
                    if (drawRef.getAll().features.length > 1) {
                        drawRef.delete(
                            drawRef
                                .getAll()
                                .features.map((feature) => feature.id)
                                .filter(
                                    (featureId) =>
                                        featureId !== latestDrawnFeatureId
                                )
                        );
                    }
                }
            }

            // 更新当前绘制模式到currentDrawMode中
            setProps({
                currentDrawMode: e.mode
            })
        },
        [drawOnlyOne]
    );

    drawRef = useControl(
        () => new MapboxDraw({ ...props, modes: _modes }),
        ({ map }) => {
            // 强制修改绘制相关控件按钮的title信息为locale相关参数所设定的文案
            // 若用户未设置localeInfo相关文案信息，则根据当前locale情况设置相应的缺省值
            for (let titles of [
                [
                    'LineString tool (l)',
                    (
                        localeInfo['DrawControl.LineStringTool'] ||
                        defaultLocaleInfo[locale]['DrawControl.LineStringTool']
                    )
                ],
                [
                    'Polygon tool (p)',
                    (
                        localeInfo['DrawControl.PolygonTool'] ||
                        defaultLocaleInfo[locale]['DrawControl.PolygonTool']
                    )
                ],
                [
                    'Marker tool (m)',
                    (
                        localeInfo['DrawControl.MarkerTool'] ||
                        defaultLocaleInfo[locale]['DrawControl.MarkerTool']
                    )
                ],
                [
                    'Delete',
                    (
                        localeInfo['DrawControl.Delete'] ||
                        defaultLocaleInfo[locale]['DrawControl.Delete']
                    )
                ],
                [
                    'Combine',
                    (
                        localeInfo['DrawControl.Combine'] ||
                        defaultLocaleInfo[locale]['DrawControl.Combine']
                    )
                ],
                [
                    'Uncombine',
                    (
                        localeInfo['DrawControl.Uncombine'] ||
                        defaultLocaleInfo[locale]['DrawControl.Uncombine']
                    )
                ],
            ]) {
                document
                    .querySelectorAll(`[title="${titles[0]}"]`)
                    .forEach((e) => e.setAttribute('title', titles[1]));
            }
            map.on('draw.create', onUpdate);
            map.on('draw.update', onUpdate);
            map.on('draw.delete', onDelete);
            map.on('draw.modechange', onModeChange);
        },
        ({ map }) => {
            map.off('draw.create', onUpdate);
            map.off('draw.update', onUpdate);
            map.off('draw.delete', onDelete);
            map.off('draw.modechange', onModeChange);
        },
        {
            position: position,
        }
    );

    useEffect(() => {
        if (drawDeleteAll) {
            if (drawRef) {
                drawRef.deleteAll()
            }
            // 重置drawDeleteAll
            setProps({
                drawDeleteAll: false,
                drawnFeatures: [] // 清空已绘制要素信息
            })
        }
    }, [drawDeleteAll])

    useEffect(() => {
        if (drawDeleteSelected) {
            if (drawRef) {
                drawRef.trash()
            }
            // 重置drawDeleteSelected
            setProps({
                drawDeleteSelected: false
            })
        }
    }, [drawDeleteSelected])

    useEffect(() => {
        if (drawRef && setDrawMode) {

            if (setDrawMode === 'simple_select') {
                // 快捷选中所有已绘制要素
                drawRef.changeMode(setDrawMode, { featureIds: drawRef.getAll().features?.map(g => g.id) })
            } else {
                // 取得当前全部图层的id并仅保留gl-draw*相关图层
                let allDrawLayerIds = mapRef.current.getStyle().layers.map(layer => layer.id).filter(layerId => layerId.startsWith('gl-draw'));
                // 针对相关图层按照原始顺序调整图层至顶层
                allDrawLayerIds.forEach(layerId => mapRef.current.moveLayer(layerId))
                drawRef.changeMode(setDrawMode);
            }
            // 重置
            setProps({
                setDrawMode: null
            })
        }
    }, [setDrawMode])

    return null;
};

const MapContainer = (props) => {
    const {
        id,
        children,
        key,
        style,
        cursor,
        mapStyle,
        renderWorldCopies,
        initialViewState,
        longitude,
        latitude,
        zoom,
        pitch,
        bearing,
        minZoom,
        maxZoom,
        minPitch,
        maxPitch,
        maxBounds,
        boxZoom,
        doubleClickZoom,
        dragRotate,
        dragPan,
        keyboard,
        scrollZoom,
        touchPitch,
        clickListenLayerIds,
        clickListenBoxSize,
        enableDraw,
        drawnFeatures,
        drawControls,
        setDrawMode,
        drawControlsPosition,
        drawOnlyOne,
        drawCircleSteps,
        enableDrawSpatialJudge,
        drawSpatialJudgePredicate,
        drawSpatialJudgeListenLayerIds,
        drawDeleteAll,
        drawDeleteSelected,
        locale,
        localeInfo,
        interactive,
        workerCount,
        debounceWait,
        debug,
        mapboxAccessToken,
        terrain,
        clickListenLayerCount,
        setProps,
    } = props;

    // 地图ref
    const mapRef = useRef(null);

    // 初始化prop同步
    useEffect(() => {
        let toUpdateProps = {};
        // 若初始化时initialViewState有效，则为相关受控prop初始化有效值
        if (initialViewState) {
            for (let propName of [
                'longitude',
                'latitude',
                'zoom',
                'pitch',
                'bearing',
            ]) {
                if (initialViewState[propName] || initialViewState[propName] === 0) {
                    toUpdateProps[propName] = initialViewState[propName];
                    toUpdateProps[propName + 'Debounce'] = initialViewState[propName];
                }
            }
        }

        // 统一初始化prop
        setProps(toUpdateProps);
    }, []);

    useEffect(() => {
        if (!drawnFeatures || drawnFeatures.length === 0) {
            setProps({
                drawSpatialJudgeListenLayerFeatures: []
            })
        }
    }, [drawnFeatures])

    // 事件监听函数
    const listenViewState = (e) => {
        // 调试模式
        if (debug) {
            console.log(
                {
                    longitude: Number(e.viewState.longitude.toFixed(6)),
                    latitude: Number(e.viewState.latitude.toFixed(6)),
                    zoom: Number(e.viewState.zoom.toFixed(3)),
                    pitch: Number(e.viewState.pitch.toFixed(3)),
                    bearing: Number(e.viewState.bearing.toFixed(3)),
                }
            )
        }
        setProps({
            longitude: Number(e.viewState.longitude.toFixed(6)),
            latitude: Number(e.viewState.latitude.toFixed(6)),
            zoom: Number(e.viewState.zoom.toFixed(3)),
            pitch: Number(e.viewState.pitch.toFixed(3)),
            bearing: Number(e.viewState.bearing.toFixed(3)),
        });
    };
    const { run: listenViewStateDebounce } = useRequest(
        (e) => {
            // 获取最新的底图bounds范围
            let currentBounds = mapRef.current.getBounds()
            setProps({
                longitudeDebounce: Number(e.viewState.longitude.toFixed(6)),
                latitudeDebounce: Number(e.viewState.latitude.toFixed(6)),
                zoomDebounce: Number(e.viewState.zoom.toFixed(3)),
                pitchDebounce: Number(e.viewState.pitch.toFixed(3)),
                bearingDebounce: Number(e.viewState.bearing.toFixed(3)),
                boundsDebounce: [
                    currentBounds._sw.lng,
                    currentBounds._sw.lat,
                    currentBounds._ne.lng,
                    currentBounds._ne.lat
                ]
            });
        },
        {
            debounceWait: debounceWait,
            manual: true,
        }
    );
    const { run: listenSourceLayerLoad } = useRequest(
        () => {
            if (debug) {
                console.log('loadedSources: ', mapRef.current.getStyle().sources)
                console.log('loadedLayers: ', mapRef.current.getStyle().layers)
            }
            setProps({
                loadedSources: mapRef.current.getStyle().sources,
                loadedLayers: mapRef.current.getStyle().layers,
            });
        },
        {
            debounceWait: debounceWait,
            manual: true,
        }
    );

    return (
        <MapGL
            ref={mapRef}
            id={id}
            key={key}
            style={style}
            cursor={cursor}
            mapStyle={mapStyle}
            renderWorldCopies={renderWorldCopies}
            initialViewState={initialViewState}
            longitude={longitude}
            latitude={latitude}
            zoom={zoom}
            pitch={pitch}
            bearing={bearing}
            minZoom={minZoom}
            maxZoom={maxZoom}
            minPitch={minPitch}
            maxPitch={maxPitch}
            maxBounds={maxBounds}
            boxZoom={boxZoom}
            doubleClickZoom={doubleClickZoom}
            dragRotate={dragRotate}
            dragPan={dragPan}
            keyboard={keyboard}
            scrollZoom={scrollZoom}
            touchPitch={touchPitch}
            locale={
                // 去除DrawControl相关键值对属性
                {
                    ...omitBy(defaultLocaleInfo[locale], (v, k) => k.startsWith('DrawControl')),
                    ...omitBy(localeInfo, (v, k) => k.startsWith('DrawControl'))
                }
            }
            interactive={interactive}
            workerCount={workerCount}
            // 事件监听
            onMove={(e) => {
                // 同步地图视角
                listenViewState(e);
                // 防抖监听地图视角
                listenViewStateDebounce(e);
            }}
            onClick={(e) => {
                if (cancelIdleCallback) {
                    // 根据点击位置对指定图层进行空间查询
                    // 构造查询范围
                    let bbox = [
                        [
                            e.point.x - clickListenBoxSize,
                            e.point.y - clickListenBoxSize,
                        ],
                        [
                            e.point.x + clickListenBoxSize,
                            e.point.y + clickListenBoxSize,
                        ],
                    ];

                    // 基于查询范围判断发生相交的要素信息数组
                    let matchFeatures = mapRef.current.queryRenderedFeatures(
                        bbox,
                        {
                            layers: clickListenLayerIds.filter((e) =>
                                mapRef.current.getLayer(e)
                            ),
                        }
                    );

                    setProps({
                        // 更新点击事件匹配到的要素信息数组
                        clickListenLayerFeatures: matchFeatures.map((f) => {
                            return {
                                layer: {
                                    id: f.layer.id,
                                    source: f.layer.source,
                                    sourceLayer: f.layer['source-layer'],
                                    type: f.layer.type,
                                },
                                properties: f.properties,
                                source: f.properties,
                                sourceLayer: f.sourceLayer,
                                type: f.type,
                                geometry: f.geometry,
                                // 记录点击位置对应的地图像素坐标
                                x: e.point.x,
                                y: e.point.y
                            };
                        }),
                        clickListenLayerCount: clickListenLayerCount + 1
                    });
                }

                setProps({
                    // 监听地图点击事件
                    clickedLngLat: {
                        lng: Number(e.lngLat.lng.toFixed(6)),
                        lat: Number(e.lngLat.lat.toFixed(6)),
                        timestamp: new Date().getTime(),
                    },
                });
            }}
            onStyleData={listenSourceLayerLoad}
            mapLib={maplibregl}
            mapboxAccessToken={mapboxAccessToken}
            terrain={terrain}
        >
            {children}
            {enableDraw ? (
                <DrawControl
                    position={drawControlsPosition}
                    displayControlsDefault={false}
                    controls={{
                        ...defaultExactProps.drawControls,
                        ...drawControls
                    }}
                    locale={locale}
                    localeInfo={localeInfo}
                    drawOnlyOne={drawOnlyOne}
                    enableDrawSpatialJudge={enableDrawSpatialJudge}
                    drawSpatialJudgePredicate={drawSpatialJudgePredicate}
                    drawSpatialJudgeListenLayerIds={drawSpatialJudgeListenLayerIds}
                    drawDeleteAll={drawDeleteAll}
                    drawDeleteSelected={drawDeleteSelected}
                    setDrawMode={setDrawMode}
                    drawCircleSteps={drawCircleSteps}
                    setProps={setProps}
                    mapRef={mapRef}
                />
            ) : null}
        </MapGL>
    );
};


MapContainer.propTypes = {
    // 基础参数
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * 设置内部组件元素，从而实现更多地图定制化功能
     */
    children: PropTypes.node,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 用于设置当前地图容器的css样式
     */
    style: PropTypes.object,

    /**
     * 设置默认鼠标指针样式，同css中的cursor属性
     * 参考资料：https://developer.mozilla.org/en-US/docs/Web/CSS/cursor
     */
    cursor: PropTypes.string,

    // 样式相关参数
    /**
     * 用于设置底图样式配置文件
     */
    mapStyle: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),

    /**
     * 设置世界范围是否允许重复
     * 默认：true
     */
    renderWorldCopies: PropTypes.bool,

    // 地图视角相关参数
    /**
     * 非受控参数，设置当前地图容器的初始视角相关参数
     * 参考资料：https://visgl.github.io/react-map-gl/docs/api-reference/map#initialviewstate
     */
    initialViewState: PropTypes.exact({
        /**
         * 用于设置初始视角对应地图中心点经度
         * 默认：0
         */
        longitude: PropTypes.number,

        /**
         * 用于设置初始视角对应地图中心点纬度
         * 默认：0
         */
        latitude: PropTypes.number,

        /**
         * 用于设置初始视角对应地图缩放级别
         * 默认：0
         */
        zoom: PropTypes.number,

        /**
         * 用于设置初始视角对应地图倾斜角度
         * 默认：0
         */
        pitch: PropTypes.number,

        /**
         * 用于设置初始视角对应地图旋转角度
         * 默认：0
         */
        bearing: PropTypes.number,

        /**
         * 用于设置初始视角对应地图视角坐标范围
         * 此项设置后会忽略已设置的longitude、latitude、zoom
         * 格式为[经度下限, 纬度下限, 经度上限, 纬度上限]
         * 默认：null
         */
        bounds: PropTypes.array,
    }),

    /**
     * 受控参数，用于设置或监听当前地图中心点经度
     */
    longitude: PropTypes.number,

    /**
     * 受控参数，用于设置或监听当前地图中心点纬度
     */
    latitude: PropTypes.number,

    /**
     * 受控参数，用于设置或监听当前地图缩放级别
     */
    zoom: PropTypes.number,

    /**
     * 受控参数，用于设置或监听当前地图倾斜角度
     */
    pitch: PropTypes.number,

    /**
     * 受控参数，用于设置或监听当前地图旋转角度
     */
    bearing: PropTypes.number,

    /**
     * 用于设置当前地图最小缩放级别，取值应在0到24之间
     * 默认：0
     */
    minZoom: PropTypes.number,

    /**
     * 用于设置当前地图最大缩放级别，取值应在0到24之间
     * 默认：22
     */
    maxZoom: PropTypes.number,

    /**
     * 用于设置当前地图最小倾斜角度，取值应在0到85之间
     * 默认：0
     */
    minPitch: PropTypes.number,

    /**
     * 用于设置当前地图最大倾斜角度，取值应在0到85之间
     * 默认：60
     */
    maxPitch: PropTypes.number,

    /**
     * 用于限制当前地图视角坐标范围，用于限制用户可查看地图范围
     * 格式为[经度下限, 纬度下限, 经度上限, 纬度上限]
     * 默认：null
     */
    maxBounds: PropTypes.array,

    // 地图交互相关参数
    /**
     * 用于设置是否开启框选放大功能，开启后用户可按住shift用鼠标在地图上绘制方框进行快速放大
     * 默认：false
     */
    boxZoom: PropTypes.bool,

    /**
     * 用于设置是否允许双击放大地图
     * 默认：true
     */
    doubleClickZoom: PropTypes.bool,

    /**
     * 用于设置是否允许鼠标拖拽旋转地图
     * 默认：true
     */
    dragRotate: PropTypes.bool,

    /**
     * 设置是否允许鼠标拖拽平移地图
     * 默认：true
     */
    dragPan: PropTypes.bool,

    /**
     * 设置是否允许通过键盘调整地图
     * 默认：true
     */
    keyboard: PropTypes.bool,

    /**
     * 设置是否允许鼠标滚轮缩放地图
     * 默认：true
     */
    scrollZoom: PropTypes.bool,

    /**
     * 设置是否允许鼠标拖拽调整地图倾斜角度
     * 默认：true
     */
    touchPitch: PropTypes.bool,

    /**
     * 设置通过地图交互事件允许监听的图层id数组
     * 默认：[]
     */
    clickListenLayerIds: PropTypes.array,

    /**
     * 设置通过地图点击事件针对interactiveLayerIds所指定的图层进行监听时，以鼠标点击点为中心外扩box范围的像素边长
     * 默认：5
     */
    clickListenBoxSize: PropTypes.number,

    // 绘制控件相关功能
    /**
     * 用于设置是否为当前地图启用绘制控件功能
     * 默认：false
     */
    enableDraw: PropTypes.bool,

    /**
     * 配置需要开启的功能控件种类
     */
    drawControls: PropTypes.exact({
        /**
         * 用于设置是否为当前地图绘制控件开启点绘制功能
         * 默认：true
         */
        point: PropTypes.bool,

        /**
         * 用于设置是否为当前地图绘制控件开启线绘制功能
         * 默认：true
         */
        line_string: PropTypes.bool,

        /**
         * 用于设置是否为当前地图绘制控件开启面绘制功能
         * 默认：true
         */
        polygon: PropTypes.bool,

        /**
         * 特殊绘图模式，无自带的触发控件按钮，用于设置是否为当前地图绘制控件开启圆形绘制功能
         * 默认：true
         */
        draw_circle: PropTypes.bool,

        /**
         * 用于设置是否为当前地图绘制控件开启已绘制要素删除功能
         * 默认：true
         */
        trash: PropTypes.bool,

        /**
         * 用于设置是否为当前地图绘制控件开启已绘制要素组合功能
         * 默认：false
         */
        combine_features: PropTypes.bool,

        /**
         * 用于设置是否为当前地图绘制控件开启已绘制要素组合拆分功能
         * 默认：false
         */
        uncombine_features: PropTypes.bool,
    }),

    /**
     * 用于手动切换到指定地图绘制功能模式，每次成功切换模式后会重置为空
     */
    setDrawMode: PropTypes.oneOf([
        'simple_select', 'draw_line_string', 'draw_polygon', 'draw_point', 'draw_circle'
    ]),

    /**
     * 用于监听当前地图绘制功能所对应的功能模式
     */
    currentDrawMode: PropTypes.string,

    /**
     * 设置地图绘制控件显示方位
     * 可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
     * 默认：'top-left'
     */
    drawControlsPosition: PropTypes.oneOf([
        'top-right',
        'top-left',
        'bottom-right',
        'bottom-left',
    ]),

    /**
     * 设置是否在每次点击相应绘制功能按钮后清空先前的已绘制要素，从而确保同时最多存在一个已绘制要素
     * 默认：false
     */
    drawOnlyOne: PropTypes.bool,

    /**
     * 设置绘制圆形时，生成矢量中circle字段返回对应圆形矢量数据的精度，越大越精准
     * 默认：64
     */
    drawCircleSteps: PropTypes.number,

    /**
     * 用于监听通过绘图控件已绘制的要素数组
     */
    drawnFeatures: PropTypes.array,

    /**
     * 当drawOnlyOne为true时生效，用于设置是否以绘制的面要素为范围，计算与之存在拓扑关联的其他图层要素
     * 默认：false
     */
    enableDrawSpatialJudge: PropTypes.bool,

    /**
     * 用于设置已绘制面要素与其他图层拓扑关联所依据的类型
     * 可选的有'intersects'（相交）、'contains'（包含）
     * 默认：'intersects'
     */
    drawSpatialJudgePredicate: PropTypes.oneOf(['intersects', 'contains']),

    /**
     * 设置通过要素绘制空间关系判断需要监听的目标图层id数组
     * 默认：[]
     */
    drawSpatialJudgeListenLayerIds: PropTypes.array,

    /**
    * 用于监听最近一次已绘制面要素对应drawSpatialJudgeListenLayerIds所查询到的相关图层要素信息
    */
    drawSpatialJudgeListenLayerFeatures: PropTypes.array,

    /**
     * 用于手动执行已绘制要素的清空操作，每次执行清空操作后会被重置为false
     * 默认：false
     */
    drawDeleteAll: PropTypes.bool,

    /**
     * 用于手动执行对已绘制要素中，处于选择状态下的要素进行删除，每次执行删除操作后会被重置为false
     * 默认：false
     */
    drawDeleteSelected: PropTypes.bool,

    // 其他参数
    /**
     * 设置语言类型，可选的有'zh-cn'（简体中文）、'en-us'（英文）
     * 默认：'zh-cn'
     */
    locale: PropTypes.oneOf(['zh-cn', 'en-us']),

    /**
     * 自定义常用文案信息
     * 具体可设置文案键值对：
     * - NavigationControl.ZoomIn
     * - NavigationControl.ZoomOut
     * - NavigationControl.ResetBearing
     * - DrawControl.LineStringTool
     * - DrawControl.PolygonTool
     * - DrawControl.MarkerTool
     * - DrawControl.Delete
     * - DrawControl.Combine
     * - DrawControl.Uncombine
     * 其他参考资料：https://github.com/maplibre/maplibre-gl-js/blob/main/src/ui/default_locale.ts
     */
    localeInfo: PropTypes.object,

    /**
     * 设置是否开启地图交互事件监听功能
     * 默认：true
     */
    interactive: PropTypes.bool,

    /**
     * 设置开启的并行工作web worker数量
     * 默认：2
     */
    workerCount: PropTypes.number,

    // 常规监听参数
    /**
     * 用于监听最近一次地图点击事件对应的坐标信息及时间戳信息
     */
    clickedLngLat: PropTypes.exact({
        /**
         * 点击位置经度
         */
        lng: PropTypes.number,
        /**
         * 点击位置纬度
         */
        lat: PropTypes.number,
        /**
         * 点击事件对应的时间戳
         */
        timestamp: PropTypes.number,
    }),

    /**
     * 用于监听最近一次地图点击事件对应clickListenLayerIds所查询到的相关图层要素信息
     */
    clickListenLayerFeatures: PropTypes.array,

    /**
     * 用于监听有效图层要素点击事件累积次数
     * 默认：0
     */
    clickListenLayerCount: PropTypes.number,

    /**
     * 用于监听最近一次图层加载事件后全部图层源信息
     */
    loadedSources: PropTypes.object,

    /**
     * 用于监听最近一次图层加载事件后全部图层信息
     */
    loadedLayers: PropTypes.array,

    // 防抖监听参数
    /**
     * 设置针对当前地图容器的防抖延时，单位：毫秒
     * 默认：200
     */
    debounceWait: PropTypes.number,

    /**
     * 防抖监听参数，用于监听当前地图中心点经度
     */
    longitudeDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于监听当前地图中心点纬度
     */
    latitudeDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于监听当前地图缩放级别
     */
    zoomDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于监听当前地图倾斜角度
     */
    pitchDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于监听当前地图旋转角度
     */
    bearingDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于监听当前地图坐标范围
     * 格式为[经度下限, 纬度下限, 经度上限, 纬度上限]
     */
    boundsDebounce: PropTypes.array,

    // 其他参数
    /**
     * 开发调试专用，用于开启debug模式，开启后会在浏览器控制台打印主要事件信息
     * 默认：false
     */
    debug: PropTypes.bool,

    /**
     * 可选，用于配置mapbox服务token
     */
    mapboxAccessToken: PropTypes.string,

    /**
     * 用于配置terrain相关参数
     */
    terrain: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

MapContainer.defaultProps = {
    initialViewState: {
        longitude: 0,
        latitude: 0,
        zoom: 0,
        pitch: 0,
        bearing: 0,
    },
    renderWorldCopies: true,
    debounceWait: 200,
    minZoom: 0,
    maxZoom: 22,
    minPitch: 0,
    maxPitch: 60,
    boxZoom: false,
    doubleClickZoom: true,
    dragRotate: true,
    dragPan: true,
    keyboard: true,
    scrollZoom: true,
    touchPitch: true,
    clickListenLayerIds: [],
    clickListenBoxSize: 5,
    enableDraw: false,
    drawControlsPosition: 'top-left',
    drawOnlyOne: false,
    drawCircleSteps: 64,
    enableDrawSpatialJudge: false,
    drawSpatialJudgePredicate: 'intersects',
    drawSpatialJudgeListenLayerIds: [],
    drawDeleteAll: false,
    drawDeleteSelected: false,
    locale: 'zh-cn',
    localeInfo: {},
    interactive: true,
    workerCount: 2,
    debug: false,
    clickListenLayerCount: 0
};

export default React.memo(MapContainer);
