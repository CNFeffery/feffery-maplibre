/* eslint-disable no-empty */
/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { useMap } from 'react-map-gl/maplibre';

const findMovedLayer = (before, after) => {
    let idx = 0;
    let len = before.length;
    while ((before[idx] === after[idx] || before[idx] === after[idx + 1]) && idx < len) {
        idx++;
    }
    // 返回进行挪动的单个元素
    return before[idx];
}

const SortLayers = ({ orders = [], supremeLayers = [], setProps }) => {

    // 取得传递的地图实例
    const { current: map } = useMap();

    useEffect(() => {
        if (map && orders && orders.length !== 0) {
            try {
                // 逐轮次排序，直到整体顺序更新完成
                while (true) {
                    // 提取当前已加载图层中与orders相关的图层
                    let relatedLayers = map.getLayersOrder().filter(layerId => orders.includes(layerId));
                    // 若当前轮次中，实际的相关图层顺序与期望的图层顺序相同
                    if (relatedLayers.map((layerId, i) => layerId === orders[i]).every((item) => item)) {
                        // 终止循环
                        break;
                    }
                    // 提取supremeLayers中图层顺序最低的图层
                    let lowestSupremeLayer = map.getLayersOrder().filter(layerId => supremeLayers.includes(layerId));
                    if (lowestSupremeLayer.length !== 0) {
                        lowestSupremeLayer = lowestSupremeLayer[0];
                    } else {
                        lowestSupremeLayer = null;
                    }
                    // 搜索发生位置移动的关键图层
                    let movedLayer = findMovedLayer(relatedLayers, orders);
                    if (movedLayer) {
                        // 若关键图层位于orders的末尾
                        if (orders.indexOf(movedLayer) + 1 === orders.length) {
                            map.moveLayer(movedLayer, lowestSupremeLayer)
                        } else {
                            // 移动至当前图层对应的更高一层图层之下
                            map.moveLayer(movedLayer, orders[orders.indexOf(movedLayer) + 1])
                        }
                    }
                }
            } catch (e) {
                console.error(e)
            }
        }
        // 每次执行完成后重置orders
        setProps({
            orders: []
        });
    }, [orders]);

    return <></>;
};

SortLayers.propTypes = {
    // 基础参数
    /**
     * 必填，用于唯一标识当前组件
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 设置要针对当前地图实例中的相关图层进行重排序的顺序图层id数组，越靠后的元素在此次排序之后图层顺序越高
     * 每次新的执行完成后会自动重置为[]
     * 默认：None
     */
    orders: PropTypes.arrayOf(PropTypes.string),

    /**
     * 设置图层顺序调整目标应当限制在哪些图层之下
     * 默认：[]
     */
    supremeLayers: PropTypes.arrayOf(PropTypes.string),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(SortLayers);
