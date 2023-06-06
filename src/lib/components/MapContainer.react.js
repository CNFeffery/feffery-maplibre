/* eslint-disable react/prop-types */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect, useState, useCallback, useRef } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import {
    Map as MapGL,
    useControl
} from 'react-map-gl';
import MapboxDraw from '@mapbox/mapbox-gl-draw';
// import DeckGL from '@deck.gl/react';
import maplibregl from 'maplibre-gl';
// 其他第三方辅助
import { useRequest } from 'ahooks';
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
        bearing: 0
    }
}

const DrawControl = (props) => {

    const {
        onCreate,
        onUpdate,
        onDelete,
        position
    } = props;

    useControl(
        () => new MapboxDraw(props),
        ({ map }) => {
            map.on("draw.create", onCreate)
            map.on("draw.update", onUpdate)
            map.on("draw.delete", onDelete)
        },
        ({ map }) => {
            map.off("draw.create", onCreate)
            map.off("draw.update", onUpdate)
            map.off("draw.delete", onDelete)
        },
        {
            position: position
        }
    )

    return null
}

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
        doubleClickZoom,
        dragRotate,
        dragPan,
        keyboard,
        scrollZoom,
        touchPitch,
        clickListenLayerIds,
        clickListenBoxSize,
        enableDraw,
        mapboxAccessToken,
        locale,
        interactive,
        workerCount,
        debounceWait,
        setProps
    } = props;

    const [features, setFeatures] = useState({})

    const onUpdate = useCallback(e => {
        setFeatures(currFeatures => {
            const newFeatures = { ...currFeatures }
            for (const f of e.features) {
                newFeatures[f.id] = f
            }
            return newFeatures
        })
    }, [])

    const onDelete = useCallback(e => {
        setFeatures(currFeatures => {
            const newFeatures = { ...currFeatures }
            for (const f of e.features) {
                delete newFeatures[f.id]
            }
            return newFeatures
        })
    }, [])

    // 地图ref
    const mapRef = useRef(null);

    // 初始化prop同步
    useEffect(() => {
        let toUpdateProps = {}
        // 若初始化时initialViewState有效，则为相关受控prop初始化有效值
        if (initialViewState) {
            for (let propName of ['longitude', 'latitude', 'zoom', 'pitch', 'bearing']) {
                if (initialViewState[propName]) {
                    toUpdateProps[propName] = initialViewState[propName]
                    toUpdateProps[propName + 'Debounce'] = initialViewState[propName]
                }
            }
        }

        // 统一初始化prop
        setProps(toUpdateProps)
    }, [])

    // 事件监听函数
    const listenViewState = (e) => {
        setProps({
            longitude: Number(e.viewState.longitude.toFixed(6)),
            latitude: Number(e.viewState.latitude.toFixed(6)),
            zoom: Number(e.viewState.zoom.toFixed(3)),
            pitch: Number(e.viewState.pitch.toFixed(3)),
            bearing: Number(e.viewState.bearing.toFixed(3))
        })
    }
    const { run: listenViewStateDebounce } = useRequest(
        (e) => {
            setProps({
                longitudeDebounce: Number(e.viewState.longitude.toFixed(6)),
                latitudeDebounce: Number(e.viewState.latitude.toFixed(6)),
                zoomDebounce: Number(e.viewState.zoom.toFixed(3)),
                pitchDebounce: Number(e.viewState.pitch.toFixed(3)),
                bearingDebounce: Number(e.viewState.bearing.toFixed(3))
            })
        },
        {
            debounceWait: debounceWait,
            manual: true
        }
    )

    return (
        <MapGL ref={mapRef}
            id={id}
            key={key}
            style={style}
            cursor={cursor}
            mapStyle={mapStyle}
            renderWorldCopies={renderWorldCopies}
            initialViewState={{
                ...defaultExactProps.initialViewState,
                ...initialViewState
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
            doubleClickZoom={doubleClickZoom}
            dragRotate={dragRotate}
            dragPan={dragPan}
            keyboard={keyboard}
            scrollZoom={scrollZoom}
            touchPitch={touchPitch}
            interactiveLayerIds={clickListenLayerIds}
            mapboxAccessToken={mapboxAccessToken}
            locale={locale}
            interactive={interactive}
            workerCount={workerCount}
            // 事件监听
            onMove={(e) => {
                // 同步地图视角
                listenViewState(e)
                // 防抖监听地图视角
                listenViewStateDebounce(e)
            }}
            onClick={(e) => {

                const bbox = [
                    [e.point.x - clickListenBoxSize, e.point.y - clickListenBoxSize],
                    [e.point.x + clickListenBoxSize, e.point.y + clickListenBoxSize]
                ];

                const selectedFeatures = mapRef.current.queryRenderedFeatures(bbox, {
                    layers: clickListenLayerIds
                });
                console.log(selectedFeatures)

                setProps({
                    // 监听地图点击事件
                    clickedLngLat: {
                        lng: Number(e.lngLat.lng.toFixed(6)),
                        lat: Number(e.lngLat.lat.toFixed(6)),
                        timestamp: new Date().getTime()
                    }
                })
            }}
            mapLib={maplibregl}
        >
            {children}
            {
                enableDraw ?
                    <DrawControl
                        position="top-right"
                        displayControlsDefault={true}
                        controls={{
                            polygon: true,
                            trash: true
                        }}
                        // defaultMode="draw_polygon"
                        onCreate={onUpdate}
                        onUpdate={onUpdate}
                        onDelete={onDelete}
                    /> :
                    null
            }
        </MapGL>
    );
}

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
    mapStyle: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

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
        bounds: PropTypes.array
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

    // 其他参数
    /**
     * 用于设置是否为当前地图启用绘制控件功能
     * 默认：false
     */
    enableDraw: PropTypes.bool,

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
        timestamp: PropTypes.number
    }),

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
    setProps: PropTypes.func
};

MapContainer.defaultProps = {
    renderWorldCopies: true,
    debounceWait: 200,
    minZoom: 0,
    maxZoom: 22,
    minPitch: 0,
    maxPitch: 60,
    doubleClickZoom: true,
    dragRotate: true,
    dragPan: true,
    keyboard: true,
    scrollZoom: true,
    touchPitch: true,
    clickListenLayerIds: [],
    clickListenBoxSize: 5,
    enableDraw: false,
    interactive: true,
    workerCount: 2
};

export default React.memo(MapContainer);