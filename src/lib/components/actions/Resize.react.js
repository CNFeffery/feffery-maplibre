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

const Resize = (props) => {
    let { resize, setProps } = props;

    // 取得传递的地图实例
    const { current: map } = useMap();

    useEffect(() => {
        if (resize) {
            try {
                // 执行地图
                map.resize();
            } catch (e) {
                console.log(e.message);
            }
            //  每次执行完成后重置resize
            setProps({
                resize: false
            })
        }
    }, [resize]);

    return <></>;
};

Resize.propTypes = {
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
     * 设置为true时用于触发地图resize事件，每次执行完成后会自动重置为false
     * 默认：false
     */
    resize: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

Resize.defaultProps = {
    resize: false
};

export default React.memo(Resize);
