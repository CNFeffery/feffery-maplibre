/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { Popup as _Popup } from 'react-map-gl/maplibre';

const Popup = (props) => {
    let {
        id,
        children,
        key,
        style,
        className,
        latitude,
        longitude,
        anchor,
        maxWidth,
        closeButton,
        closeOnMove,
        closeOnClick,
        offset,
        setProps
    } = props;

    return (
        <_Popup id={id}
            key={key}
            style={style}
            className={className}
            latitude={latitude}
            longitude={longitude}
            anchor={anchor}
            maxWidth={maxWidth}
            closeButton={closeButton}
            closeOnMove={closeOnMove}
            closeOnClick={closeOnClick}
            offset={offset}
            focusAfterOpen={false}
        >
            {children}
        </_Popup>
    );
};

Popup.propTypes = {
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
     * 用于设置当前弹出卡片的css样式
     */
    style: PropTypes.object,

    /**
     * 用于设置当前弹出卡片的css类名
     */
    className: PropTypes.string,

    /**
     * 必填，设置当前标记对应位置纬度
     */
    latitude: PropTypes.number.isRequired,

    /**
     * 必填，设置当前标记对应位置经度
     */
    longitude: PropTypes.number.isRequired,

    /**
     * 当前弹出卡片相对坐标点的方位
     * 可选的有'center'、'top'、'bottom'、'left'、'right'、'top-left'、'top-right'、'bottom-left'、'bottom-right'
     * 默认：'center'
     */
    anchor: PropTypes.oneOf(['center', 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right']),

    /**
     * 设置当前弹出卡片的最大宽度
     * 默认：'240px'
     */
    maxWidth: PropTypes.string,

    /**
     * 是否显示关闭按钮
     * 默认：true
     */
    closeButton: PropTypes.bool,

    /**
     * 地图移动时是否触发关闭
     * 默认：false
     */
    closeOnMove: PropTypes.bool,

    /**
     * 点击地图其他位置是否触发关闭
     * 默认：true
     */
    closeOnClick: PropTypes.bool,

    /**
     * 设置当前弹出卡片在水平和竖直方向上需要进行的像素偏移
     * 格式如：[水平像素偏移, 竖直像素偏移]
     */
    offset: PropTypes.arrayOf(PropTypes.number),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

Popup.defaultProps = {
    maxWidth: '240px',
    closeButton: true,
    closeOnMove: false,
    closeOnClick: true
};

export default React.memo(Popup);
