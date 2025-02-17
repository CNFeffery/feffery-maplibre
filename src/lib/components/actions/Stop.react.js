/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { useMap } from 'react-map-gl/maplibre';

const Stop = ({ execute = false, delay, setProps }) => {

    // 取得传递的地图实例
    const { current: map } = useMap();

    // 每次mapActionConfig有效时执行panTo()动作
    useEffect(() => {
        if (execute) {
            if (delay) {
                // 延时执行
                setTimeout(() => {
                    map.stop();
                }, delay)
            } else {
                map.stop();
            }
            setProps({
                execute: false
            })
        }
    }, [execute])

    return <></>;
};

Stop.propTypes = {
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
     * 是否执行停止动作，默认为false，每次设置为true并成功停止动画后，会被重置为false
     */
    execute: PropTypes.bool,

    /**
     * 设置动作延时，单位：毫秒
     */
    delay: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(Stop);