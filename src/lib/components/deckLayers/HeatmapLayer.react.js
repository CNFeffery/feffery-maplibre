/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyHeatmapLayer = React.lazy(() => import(/* webpackChunkName: "deck_gl_layers" */ '../../fragments/deckLayers/HeatmapLayer.react'));

const HeatmapLayer = ({
    id,
    data,
    visible = true,
    beforeId,
    opacity = 1,
    radiusPixels = 30,
    colorRange,
    intensity = 1,
    threshold = 0.05,
    colorDomain,
    aggregation = 'SUM',
    weightsTextureSize = 2048,
    debounceTimeout = 500,
    getPosition,
    getWeight,
    setProps
}) => {
    return (
        <Suspense fallback={null}>
            <LazyHeatmapLayer {
                ...{
                    id,
                    data,
                    visible,
                    beforeId,
                    opacity,
                    radiusPixels,
                    colorRange,
                    intensity,
                    threshold,
                    colorDomain,
                    aggregation,
                    weightsTextureSize,
                    debounceTimeout,
                    getPosition,
                    getWeight,
                    setProps
                }
            } />
        </Suspense>
    );
}

HeatmapLayer.propTypes = {
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
     * 可选，设置当前图层插入已有图层位置之前所对应的图层id
     */
    beforeId: PropTypes.string,

    /**
     * 设置当前图层透明度
     * 默认：1
     */
    opacity: PropTypes.number,

    // 当前组件特有参数
    /**
     * 热力点的像素半径
     * 默认：30
     */
    radiusPixels: PropTypes.number,

    /**
     * 热力点色彩方案数组
     * 数组元素接受格式如[r, g, b, a]或[r, g, b]
     */
    colorRange: PropTypes.array,

    /**
     * 热力值强度系数，最终的热力权重值将会乘以该系数
     * 默认：1
     */
    intensity: PropTypes.number,

    /**
     * 热力值阈值
     * 默认：0.05
     */
    threshold: PropTypes.number,

    /**
     * 限定热力值范围
     * 格式如[最小值, 最大值]
     */
    colorDomain: PropTypes.arrayOf(PropTypes.number),

    /**
     * 设置针对每个像素点计算热力值使用到的聚合方式
     * 可选的有'SUM'、'MEAN'
     * 默认：'SUM'
     */
    aggregation: PropTypes.oneOf(['SUM', 'MEAN']),

    /**
     * 调节热力渲染质地细致程度，更小的值意味着更快的渲染速度
     * 默认：2048
     */
    weightsTextureSize: PropTypes.number,

    /**
     * 调节当前热力图层随地图视角更新而随之更新，对应的防抖延时时长，单位：毫秒
     * 默认：500
     */
    debounceTimeout: PropTypes.number,

    // 数据驱动视觉控制相关参数
    /**
     * 控制热力点坐标驱动方式
     */
    getPosition: PropTypes.oneOfType([
        // 传入字符串时，代表每个数据项中充当热力点坐标的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算热力点坐标的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 控制热力点权重驱动方式
     */
    getWeight: PropTypes.oneOfType([
        // 传入数值型时，直接定义固定的热力点权重
        PropTypes.number,
        // 传入字符串时，代表每个数据项中充当热力点权重的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算热力点权重的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(HeatmapLayer);

export const propTypes = HeatmapLayer.propTypes;
export const defaultProps = HeatmapLayer.defaultProps;