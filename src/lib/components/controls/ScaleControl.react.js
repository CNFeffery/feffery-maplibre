/* eslint-disable no-unused-vars */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { ScaleControl as _ScaleControl } from 'react-map-gl/maplibre';


const ScaleControl = ({
    id,
    key,
    style,
    position = 'bottom-left',
    maxWidth = 100,
    setProps
}) => {

    return (
        <_ScaleControl id={id}
            key={key}
            style={style}
            position={position}
            maxWidth={maxWidth}
        />
    );
}

ScaleControl.propTypes = {
    // 基础参数
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 用于设置当前控件容器的css样式
     */
    style: PropTypes.object,

    /**
     * 设置当前比例尺控件显示方位
     * 可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
     * 默认：'bottom-left'
     */
    position: PropTypes.oneOf(['top-right', 'top-left', 'bottom-right', 'bottom-left']),

    /**
     * 设置当前比例尺控件最大像素宽度
     * 默认：100
     */
    maxWidth: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
    */
    setProps: PropTypes.func
};

export default React.memo(ScaleControl);