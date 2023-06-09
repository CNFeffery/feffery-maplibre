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
import { bbox } from '@turf/bbox';
import { intersect } from '@turf/intersect';
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

const DrawControl = (props) => {
    let drawRef = useRef(null);
    const { position, drawOnlyOne } = props;
    const [features, setFeatures] = useState({});

    const onUpdate = useCallback((e) => {
        console.log('onUpdate');
        console.log(e);
        setFeatures((currFeatures) => {
            const newFeatures = { ...currFeatures };
            for (const f of e.features) {
                newFeatures[f.id] = f;
            }
            return newFeatures;
        });
    }, []);

    const onDelete = useCallback((e) => {
        setFeatures((currFeatures) => {
            const newFeatures = { ...currFeatures };
            for (const f of e.features) {
                delete newFeatures[f.id];
            }
            return newFeatures;
        });
    }, []);

    const OnModeChange = useCallback(
        (e) => {
            if (
                ['draw_polygon', 'draw_line_string', 'draw_point'].includes(
                    e.mode
                )
            ) {
                if (drawOnlyOne) {
                    // 开始新的要素绘制之前清除先前已绘制要素
                    let drawnFeatures = drawRef.getAll().features;
                    // 取得最新添加的要素的id
                    let latestDrawnFeatureId = drawnFeatures[drawnFeatures.length - 1].id;
                    if (drawRef.getAll().features.length > 1) {
                        drawRef.delete(
                            drawRef
                                .getAll()
                                .features
                                .map((feature) => feature.id)
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
            // 强制修改绘制相关控件按钮的title信息为中文文案
            for (let titles of [
                ['LineString tool (l)', '绘制线'],
                ['Polygon tool (p)', '绘制面'],
                ['Marker tool (m)', '绘制点'],
                ['Delete', '删除'],
                ['Combine', '组合'],
                ['Uncombine', '绘制点'],
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
        mapboxAccessToken,
        locale,
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
            locale={locale}
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
                                type: e.type,
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
                    drawOnlyOne={drawOnlyOne}
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

    // 其他参数
    /**
     * 用于设置mapbox服务对应token
     */
    mapboxAccessToken: PropTypes.string,

    /**
     * 自定义常用文案信息
     * 参考资料：https://github.com/maplibre/maplibre-gl-js/blob/main/src/ui/default_locale.ts
     */
    locale: PropTypes.object,

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
    interactive: true,
    workerCount: 2,
};

export default React.memo(MapContainer);
