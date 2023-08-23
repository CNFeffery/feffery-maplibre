/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { useMap } from 'react-map-gl/maplibre';

const SortLayers = (props) => {
    let { orders, setProps } = props;

    // 取得传递的地图实例
    const { current: map } = useMap();

    useEffect(() => {
        if (orders) {
            for (let i = 0; i < orders.length - 1; i++) {
                // 尝试进行顺序调整
                try {
                    map.moveLayer(orders[i], orders[i + 1]);
                } catch (e) {
                    console.log(e.message);
                }
            }
            // 每次执行完成后重置orders
            setProps({
                orders: [],
            });
        }
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
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

SortLayers.defaultProps = {
    orders: []
};

export default React.memo(SortLayers);
