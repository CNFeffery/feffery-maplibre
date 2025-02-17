/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { Marker as _Marker } from 'react-map-gl/maplibre';
// 其他第三方辅助
import { useRequest } from 'ahooks';

const Marker = ({
    id,
    children,
    key,
    style,
    anchor = 'center',
    color = '#3FB1CE',
    draggable = false,
    latitude,
    longitude,
    offset,
    pitchAlignment = 'auto',
    rotation = 0,
    rotationAlignment = 'auto',
    scale = 1,
    nClicks = 0,
    debounceWait = 200,
    setProps
}) => {

    // 初始化同步latitudeDebounce、longitudeDebounce
    useEffect(() => {
        setProps({
            latitudeDebounce: latitude,
            longitudeDebounce: longitude
        })
    }, [])

    const { run: listenDrag } = useRequest(
        (e) => {
            setProps({
                latitudeDebounce: Number(e.lngLat.lat.toFixed(6)),
                longitudeDebounce: Number(e.lngLat.lng.toFixed(6))
            });
        },
        {
            debounceWait: debounceWait,
            manual: true,
        }
    );

    return (
        <_Marker id={id}
            key={key}
            style={style}
            anchor={anchor}
            color={color}
            draggable={draggable}
            latitude={latitude}
            longitude={longitude}
            offset={offset}
            pitchAlignment={pitchAlignment}
            rotation={rotation}
            rotationAlignment={rotationAlignment}
            scale={scale}
            onDrag={(e) => {
                setProps({
                    latitude: Number(e.lngLat.lat.toFixed(6)),
                    longitude: Number(e.lngLat.lng.toFixed(6))
                })
                // 防抖监听更新
                listenDrag(e)
            }}
            onClick={(e) => {
                setProps({
                    nClicks: nClicks + 1
                })
            }}
        >
            {children}
        </_Marker>
    );
};

Marker.propTypes = {
    // 基础参数
    /**
     * 必填，用于唯一标识当前组件
     */
    id: PropTypes.string,

    /**
     * 设置内部元素，用于代替缺省的标记图标
     */
    children: PropTypes.node,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 用于设置当前标记容器的css样式
     */
    style: PropTypes.object,

    /**
     * 当前标记坐标点相对标记内容的方位
     * 可选的有'center'、'top'、'bottom'、'left'、'right'、'top-left'、'top-right'、'bottom-left'、'bottom-right'
     * 默认：'center'
     */
    anchor: PropTypes.oneOf(['center', 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right']),

    /**
     * 当前标记颜色
     * 默认：'#3FB1CE'
     */
    color: PropTypes.string,

    /**
     * 当前标记是否可自由拖动
     * 默认：false
     */
    draggable: PropTypes.bool,

    /**
     * 必填，设置当前标记对应位置纬度
     */
    latitude: PropTypes.number.isRequired,

    /**
     * 必填，设置当前标记对应位置经度
     */
    longitude: PropTypes.number.isRequired,

    /**
     * 设置当前标记位置在水平、竖直方向上的像素偏移
     */
    offset: PropTypes.arrayOf(PropTypes.number),

    /**
     * 设置当前标记倾斜角度的对齐方式，可选的有'map'、'viewport'、'auto'
     * 默认：'auto'
     */
    pitchAlignment: PropTypes.oneOf(['map', 'viewport', 'auto']),

    /**
     * 设置当前标记的旋转角度
     * 默认：0
     */
    rotation: PropTypes.number,

    /**
     * 设置当前标记旋转角度的对齐方式，可选的有'map'、'viewport'、'auto'
     * 默认：'auto'
     */
    rotationAlignment: PropTypes.oneOf(['map', 'viewport', 'auto']),

    /**
     * 设置当前标记的缩放倍数
     * 默认：1
     */
    scale: PropTypes.number,

    // 常规监听参数
    /**
     * 监听当前标记累计被点击次数
     */
    nClicks: PropTypes.number,

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
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(Marker);