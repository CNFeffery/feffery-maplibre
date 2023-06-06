/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { NavigationControl as _NavigationControl } from 'react-map-gl';


const NavigationControl = (props) => {
    const {
        id,
        key,
        style,
        position,
        showCompass,
        showZoom,
        visualizePitch,
        setProps
    } = props;

    return (
        <_NavigationControl id={id}
            key={key}
            style={style}
            position={position}
            showCompass={showCompass}
            showZoom={showZoom}
            visualizePitch={visualizePitch}
        />
    );
}

NavigationControl.propTypes = {
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
     * 用于设置当前地图容器的css样式
     */
    style: PropTypes.object,

    /**
     * 设置当前导航控件显示方位
     * 可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
     * 默认：'top-right'
     */
    position: PropTypes.oneOf(['top-right', 'top-left', 'bottom-right', 'bottom-left']),

    /**
     * 设置导航控件中是否显示指南针按钮
     * 默认：true
     */
    showCompass: PropTypes.bool,

    /**
     * 设置导航控件中是否显示缩放按钮
     * 默认：true
     */
    showZoom: PropTypes.bool,

    /**
     * 设置导航控件中的指南针图标是否展示地图倾斜状态
     * 默认：false
     */
    visualizePitch: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
    */
    setProps: PropTypes.func
};

NavigationControl.defaultProps = {
    position: 'top-right',
    showCompass: true,
    showZoom: true,
    visualizePitch: false
};

export default React.memo(NavigationControl);