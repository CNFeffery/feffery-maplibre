/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyGeoJsonLayer = React.lazy(() => import(/* webpackChunkName: "deck_gl_layers" */ '../../fragments/deckLayers/GeoJsonLayer.react'));

const GeoJsonLayer = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyGeoJsonLayer {...props} />
        </Suspense>
    );
}

GeoJsonLayer.propTypes = {
    // 基础参数
    /**
     * 用于唯一标识当前图层
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 为当前图层设置数据源，当传入字符串时，代表数据源对应的url地址
     * 默认：[]
     */
    data: PropTypes.oneOfType([
        PropTypes.array,
        PropTypes.string
    ]),

    /**
     * 设置当前图层是否可见
     * 默认：true
     */
    visible: PropTypes.bool,

    /**
     * 设置当前图层透明度
     * 默认：1
     */
    opacity: PropTypes.number,

    /**
     * 设置是否启用鼠标交互事件
     * 默认：false
     */
    pickable: PropTypes.bool,

    /**
     * 设置鼠标悬停要素高亮色
     * 接受格式如[r, g, b, a]或[r, g, b]
     * 默认：[0, 0, 128, 128]
     */
    highlightColor: PropTypes.array,

    /**
     * 当pickable为true时有效，用于设置是否自动高亮鼠标悬停的要素
     * 默认：false
     */
    autoHighlight: PropTypes.bool,

    /**
     * 用于动态构造鼠标悬停tooltip内容的js函数字符串
     */
    tooltipRenderer: PropTypes.string,

    // 当前组件特有参数
    /**
     * 设置针对点要素进行渲染的类型，可选的有'circle'、'icon'、'text'
     * 也可以同时使用多种类型组合，用'+'连接，譬如：'icon+text'
     * 默认：'circle'
     */
    pointType: PropTypes.oneOf(['circle', 'icon', 'text']),

    /**
     * 设置是否针对要素中的多边形及渲染为圆圈的点要素进行填充绘制
     * 默认：true
     */
    filled: PropTypes.bool,

    /**
     * 设置是否针对要素中的多边形及渲染为圆圈的点要素进行轮廓绘制
     * 默认：false
     */
    stroked: PropTypes.bool,

    /**
     * 针对线要素及其他要素的轮廓线，设置宽度值对应的单位
     * 可选的有'meters'、'common'、'pixels'
     * 默认：'pixels'
     * 参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units
     */
    lineWidthUnits: PropTypes.oneOf(['meters', 'common', 'pixels']),

    /**
     * 针对线要素及其他要素的轮廓线，设置宽度扩张系数
     * 默认：1
     */
    lineWidthScale: PropTypes.number,

    /**
     * 针对线要素及其他要素的轮廓线，设置线条最小显示宽度，单位：像素
     * 默认：1
     */
    lineWidthMinPixels: PropTypes.number,

    /**
     * 针对线要素及其他要素的轮廓线，设置线条最大显示宽度，单位：像素
     * 默认无限制
     */
    lineWidthMaxPixels: PropTypes.number,

    /**
     * 针对线要素及其他要素的轮廓线，设置线条是否随着视角变化，而始终面朝屏幕视角
     * 默认：false
     */
    lineBillboard: PropTypes.bool,

    /**
     * 针对多边形，设置是否进行高度拉伸，配合getElevation参数使用
     * 默认：false
     */
    extruded: PropTypes.bool,

    /**
     * extruded=true时，设置是否为进行高度拉伸的要素渲染边框
     * 默认：false
     */
    wireframe: PropTypes.bool,

    /**
     * extruded为true时有效，设置高度拉伸系数
     * 默认：1
     */
    elevationScale: PropTypes.number,

    // 点要素渲染相关参数
    /**
     * pointType='circle'时有效，设置圆圈半径对应的单位
     * 可选的有'meters'、'common'、'pixels'
     * 默认：'pixels'
     * 参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units
     */
    pointRadiusUnits: PropTypes.oneOf(['meters', 'common', 'pixels']),

    /**
     * pointType='circle'时有效，设置圆圈半径扩张系数
     * 默认：1
     */
    pointRadiusScale: PropTypes.number,

    /**
     * pointType='circle'时有效，设置圆圈最小显示半径，单位：像素
     * 默认：1
     */
    pointRadiusMinPixels: PropTypes.number,

    /**
     * pointType='circle'时有效，设置圆圈最大显示半径，单位：像素
     * 默认无限制
     */
    pointRadiusMaxPixels: PropTypes.number,

    /**
     * pointType='circle'时有效，设置圆圈是否随着视角变化，而始终面朝屏幕视角
     * 默认：false
     */
    pointBillboard: PropTypes.bool,

    // 数据驱动视觉控制相关参数
    /**
     * filled=true时，针对要素中的多边形及渲染为圆圈的点要素，控制填充颜色驱动方式
     * 默认：[0, 0, 0, 255]
     */
    getFillColor: PropTypes.oneOfType([
        // 传入数组时，用于直接定义[r, g, b, a]或[r, g, b]格式颜色值
        PropTypes.array,
        // 传入字符串时，代表每个数据项中充当要素填充颜色的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算要素填充颜色的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 针对线要素及其他要素轮廓线，控制线条颜色驱动方式
     */
    getLineColor: PropTypes.oneOfType([
        // 传入数组时，用于直接定义[r, g, b, a]或[r, g, b]格式颜色值
        PropTypes.array,
        // 传入字符串时，代表每个数据项中充当线条颜色的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算线条颜色的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 针对线要素及其他要素轮廓线，控制线条宽度驱动方式
     * 默认：1
     */
    getLineWidth: PropTypes.oneOfType([
        // 传入数值型时，直接定义与lineWidthUnits对应的固定宽度值
        PropTypes.number,
        // 传入字符串时，代表每个数据项中充当线条宽度的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算线条宽度的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * extruded=true时，针对拉伸高度的多边形，控制高度驱动方式
     * 默认：1000
     */
    getElevation: PropTypes.oneOfType([
        // 传入数值型时，直接定义拉伸高度
        PropTypes.number,
        // 传入字符串时，代表每个数据项中充当拉伸高度的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算拉伸高度的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 针对以圆圈形式渲染的点要素，控制圆圈半径驱动方式
     * 默认：1
     */
    getPointRadius: PropTypes.oneOfType([
        // 传入数值型时，直接定义与pointRadiusUnits对应的固定半径值
        PropTypes.number,
        // 传入字符串时，代表每个数据项中充当半径的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算半径的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    // 事件监听相关参数
    /**
     * 设置事件监听防抖延时，单位：毫秒
     * 默认：200
     */
    debounceWait: PropTypes.number,

    /**
     * 监听鼠标悬停事件相关参数
     */
    hoverEvent: PropTypes.object,

    /**
     * 监听鼠标点击事件相关参数
     */
    clickEvent: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

GeoJsonLayer.defaultProps = {
    visible: true,
    opacity: 1,
    pickable: false,
    highlightColor: [0, 0, 128, 128],
    autoHighlight: false,
    pointType: 'circle',
    filled: true,
    stroked: true,
    lineWidthUnits: 'pixels',
    lineWidthScale: 1,
    lineWidthMinPixels: 1,
    lineBillboard: false,
    extruded: false,
    wireframe: false,
    elevationScale: 1,
    pointRadiusUnits: 'meters',
    pointRadiusScale: 1,
    pointRadiusMinPixels: 0,
    pointBillboard: false,
    getFillColor: [0, 0, 0, 255],
    getLineColor: [0, 0, 0, 255],
    getLineWidth: 1,
    getElevation: 1000,
    getPointRadius: 1,
    debounceWait: 200
};

export default React.memo(GeoJsonLayer);

export const propTypes = GeoJsonLayer.propTypes;
export const defaultProps = GeoJsonLayer.defaultProps;