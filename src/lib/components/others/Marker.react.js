/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { Marker as _Marker } from 'react-map-gl';

const Marker = (props) => {
    let {
        id,
        children,
        key,
        style,
        color,
        draggable,
        latitude,
        longitude,
        offset,
        pitchAlignment,
        rotation,
        rotationAlignment,
        scale,
        setProps
    } = props;

    return (
        <_Marker id={id}
            key={key}
            style={style}
            color={color}
            draggable={draggable}
            latitude={latitude}
            longitude={longitude}
            offset={offset}
            pitchAlignment={pitchAlignment}
            rotation={rotation}
            rotationAlignment={rotationAlignment}
            scale={scale}
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

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

Marker.defaultProps = {
    color: '#3FB1CE',
    draggable: false,
    pitchAlignment: 'auto',
    rotation: 0,
    rotationAlignment: 'auto',
    scale: 1
};

export default React.memo(Marker);
