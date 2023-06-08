/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import {useMap} from 'react-map-gl';

const HandleRawMap = (props) => {
    let {jsString, setProps} = props;

    // 取得传递的地图实例
    const {current: map} = useMap();

    useEffect(() => {
        if (jsString) {
            // 尝试直接执行最近更新的jsString
            try {
                eval(jsString);
            } catch (e) {
                console.log(e.message);
            }
            // 每次执行完成后重置jsString
            setProps({
                jsString: null,
            });
        }
    }, [jsString]);

    return <></>;
};

HandleRawMap.propTypes = {
    // 基础参数
    /**
     * 必填，用于唯一标识当前图层
     */
    id: PropTypes.string.isRequired,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 设置要针对当前地图实例中的map对象执行的javascript代码字符串
     * 每次新的执行完成后会自动重置为null
     * 默认：None
     */
    jsString: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

HandleRawMap.defaultProps = {};

export default React.memo(HandleRawMap);
