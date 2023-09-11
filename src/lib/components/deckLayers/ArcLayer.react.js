/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
// deck.gl相关
import { ArcLayer as _ArcLayer } from '@deck.gl/layers';

const LazyArcLayer = React.lazy(() => import(/* webpackChunkName: "arc_layer" */ '../../fragments/deckLayers/ArcLayer.react'));

const ArcLayer = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyArcLayer {...props} />
        </Suspense>
    );
}

ArcLayer.propTypes = {
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
     * 是否启用大圆弧线模式
     * 默认：false
     */
    greatCircle: PropTypes.bool,

    /**
     * 设置每段弧线的分段数量，越大弧线越接近曲线
     * 默认：50
     */
    numSegments: PropTypes.number,

    /**
     * 设置宽度单位，可选的有'meters'、'common'、'pixels'
     * 默认：'pixels'
     * 参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units
     */
    widthUnits: PropTypes.oneOf(['meters', 'common', 'pixels']),

    /**
     * 设置宽度扩张系数
     * 默认：1
     */
    widthScale: PropTypes.number,

    /**
     * 设置弧线最小显示宽度，单位：像素
     * 默认：1
     */
    widthMinPixels: PropTypes.number,

    /**
     * 设置弧线最大显示宽度，单位：像素
     * 默认无限制
     */
    widthMaxPixels: PropTypes.number,

    // 数据驱动视觉控制相关参数
    /**
     * 控制弧线起点坐标驱动方式
     */
    getSourcePosition: PropTypes.oneOfType([
        // 传入字符串时，代表每个数据项中充当弧线起点坐标的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算弧线起点坐标的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 控制弧线终点坐标驱动方式
     */
    getTargetPosition: PropTypes.oneOfType([
        // 传入字符串时，代表每个数据项中充当弧线终点坐标的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算弧线终点坐标的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 控制弧线起点颜色驱动方式
     */
    getSourceColor: PropTypes.oneOfType([
        // 传入数组时，用于直接定义[r, g, b, a]或[r, g, b]格式颜色值
        PropTypes.array,
        // 传入字符串时，代表每个数据项中充当弧线起点颜色的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算弧线起点颜色的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 控制弧线终点颜色驱动方式
     */
    getTargetColor: PropTypes.oneOfType([
        // 传入数组时，用于直接定义[r, g, b, a]或[r, g, b]格式颜色值
        PropTypes.array,
        // 传入字符串时，代表每个数据项中充当弧线终点颜色的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算弧线终点颜色的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 控制弧线宽度驱动方式
     */
    getWidth: PropTypes.oneOfType([
        // 传入数值型时，直接定义与widthUnits对应的固定宽度值
        PropTypes.number,
        // 传入字符串时，代表每个数据项中充当弧线宽度的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算弧线宽度的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 控制弧线高度系数驱动方式
     */
    getHeight: PropTypes.oneOfType([
        // 传入数值型时，直接定义弧线高度系数
        PropTypes.number,
        // 传入字符串时，代表每个数据项中充当弧线高度系数的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算弧线高度系数的js函数
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 控制弧线微调系数驱动方式，用于解决相同起点终点的多条弧线相互重叠的问题
     * 参数值应在-90到90之间，单位：度
     */
    getTilt: PropTypes.oneOfType([
        // 传入数值型时，直接定义弧线微调系数
        PropTypes.number,
        // 传入字符串时，代表每个数据项中充当弧线微调系数的属性路径规则
        PropTypes.string,
        // 传入具有func字段的字典时，设置用于根据每个数据项计算弧线微调系数的js函数
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

ArcLayer.defaultProps = {
    visible: true,
    opacity: 1,
    pickable: false,
    highlightColor: [0, 0, 128, 128],
    autoHighlight: false,
    greatCircle: false,
    numSegments: 50,
    widthUnits: 'pixels',
    widthScale: 1,
    widthMinPixels: 1,
    debounceWait: 200
};

export default React.memo(ArcLayer);

export const propTypes = ArcLayer.propTypes;
export const defaultProps = ArcLayer.defaultProps;