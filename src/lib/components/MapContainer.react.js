/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect, useState, useCallback, useRef } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { Map as MapGL, useControl } from 'react-map-gl';
import MapboxDraw from '@mapbox/mapbox-gl-draw';
// import DeckGL from '@deck.gl/react';
import maplibregl from 'maplibre-gl';
// 其他第三方辅助
import { useRequest } from 'ahooks';
import bbox from '@turf/bbox';
import intersects from '@turf/boolean-intersects';
import contains from '@turf/boolean-contains';
import pickBy from 'lodash/pickBy';
import omitBy from 'lodash/omitBy';
// 依赖库相关样式
import 'maplibre-gl/dist/maplibre-gl.css';
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css';
// 自定义样式
import '../css/base.css';

// 定义部分exact型prop的默认值
const defaultExactProps = {
    initialViewState: {
        longitude: 0,
        latitude: 0,
        zoom: 0,
        pitch: 0,
        bearing: 0,
    },
    drawControls: {
        point: true,
        line_string: true,
        polygon: true,
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
        enableDrawSpatialJudge,
        drawSpatialJudgePredicate,
        drawSpatialJudgeListenLayerIds,
        setProps,
        mapRef
    } = props;

    const onUpdate = useCallback((e) => {

        // 提取最新绘制的面要素
        let _drawnFeatures = drawRef.getAll().features;
        let latestDrawnFeature = _drawnFeatures[_drawnFeatures.length - 1];

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
                (feature) => drawSpatialJudgePredicate === 'intersects' ?
                    intersects(latestDrawnFeature, feature) :
                    contains(latestDrawnFeature, feature)
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
            drawnFeatures: [...drawRef.getAll().features]
        })
    }, []);

    const onDelete = useCallback((e) => {
    }, []);

    const OnModeChange = useCallback(
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
        },
        [drawOnlyOne]
    );

    drawRef = useControl(
        () => new MapboxDraw(props),
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
            map.on('draw.modechange', OnModeChange);
        },
        ({ map }) => {
            map.off('draw.create', onUpdate);
            map.off('draw.update', onUpdate);
            map.off('draw.delete', onDelete);
            map.off('draw.modechange', OnModeChange);
        },
        {
            position: position,
        }
    );

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
        drawControls,
        drawControlsPosition,
        drawOnlyOne,
        enableDrawSpatialJudge,
        drawSpatialJudgePredicate,
        drawSpatialJudgeListenLayerIds,
        mapboxAccessToken,
        locale,
        localeInfo,
        interactive,
        workerCount,
        debounceWait,
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
                if (initialViewState[propName]) {
                    toUpdateProps[propName] = initialViewState[propName];
                    toUpdateProps[propName + 'Debounce'] =
                        initialViewState[propName];
                }
            }
        }

        // 统一初始化prop
        setProps(toUpdateProps);
    }, []);

    // 事件监听函数
    const listenViewState = (e) => {
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
            setProps({
                longitudeDebounce: Number(e.viewState.longitude.toFixed(6)),
                latitudeDebounce: Number(e.viewState.latitude.toFixed(6)),
                zoomDebounce: Number(e.viewState.zoom.toFixed(3)),
                pitchDebounce: Number(e.viewState.pitch.toFixed(3)),
                bearingDebounce: Number(e.viewState.bearing.toFixed(3)),
            });
        },
        {
            debounceWait: debounceWait,
            manual: true,
        }
    );
    const { run: listenSourceLayerLoad } = useRequest(
        () => {
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
            initialViewState={{
                ...defaultExactProps.initialViewState,
                ...initialViewState,
            }}
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
            mapboxAccessToken={mapboxAccessToken}
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
                        clickListenLayerFeatures: matchFeatures.map((e) => {
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
                                type: e.type
                            };
                        }),
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
        >
            {children}
            {enableDraw ? (
                <DrawControl
                    position={drawControlsPosition}
                    displayControlsDefault={false}
                    controls={{
                        ...defaultExactProps.drawControls,
                        ...drawControls,
                    }}
                    locale={locale}
                    localeInfo={localeInfo}
                    drawOnlyOne={drawOnlyOne}
                    enableDrawSpatialJudge={enableDrawSpatialJudge}
                    drawSpatialJudgePredicate={drawSpatialJudgePredicate}
                    drawSpatialJudgeListenLayerIds={drawSpatialJudgeListenLayerIds}
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

    // 其他参数
    /**
     * 用于设置mapbox服务对应token
     */
    mapboxAccessToken: PropTypes.string,

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
     * 防抖监听参数，用于设置或监听当前地图中心点纬度
     */
    latitudeDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于设置或监听当前地图缩放级别
     */
    zoomDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于设置或监听当前地图倾斜角度
     */
    pitchDebounce: PropTypes.number,

    /**
     * 防抖监听参数，用于设置或监听当前地图旋转角度
     */
    bearingDebounce: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

MapContainer.defaultProps = {
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
    enableDrawSpatialJudge: false,
    drawSpatialJudgePredicate: 'intersects',
    drawSpatialJudgeListenLayerIds: [],
    locale: 'zh-cn',
    localeInfo: {},
    interactive: true,
    workerCount: 2,
};

export default React.memo(MapContainer);
