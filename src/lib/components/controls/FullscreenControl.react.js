/* eslint-disable no-unused-vars */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { FullscreenControl as _FullscreenControl } from 'react-map-gl/maplibre';


const FullscreenControl = ({
    id,
    key,
    style,
    position = 'top-right',
    setProps
}) => {

    return (
        <_FullscreenControl id={id}
            key={key}
            style={style}
            position={position}
        />
    );
}

FullscreenControl.propTypes = {
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
     * 设置当前全屏控件显示方位
     * 可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
     * 默认：'top-right'
     */
    position: PropTypes.oneOf(['top-right', 'top-left', 'bottom-right', 'bottom-left']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
    */
    setProps: PropTypes.func
};

export default React.memo(FullscreenControl);