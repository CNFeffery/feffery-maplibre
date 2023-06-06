/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { Layer as _Layer } from 'react-map-gl';


const Layer = (props) => {
    const {
        id,
        key,
        beforeId,
        layerProps,
        setProps
    } = props;

    return (
        <_Layer id={id}
            key={key}
            beforeId={beforeId}
            {...layerProps} />
    );
}

Layer.propTypes = {
    // 基础参数
    /**
     * 必填，用于唯一标识当前矢量切片图层
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 当需要动态更新覆盖已有矢量切片图层时，用于指定对应已有矢量切片图层的id
     */
    beforeId: PropTypes.string,

    /**
     * 设置其他layer相关配置参数
     * 参考资料：https://maplibre.org/maplibre-style-spec/layers/
     */
    layerProps: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
    */
    setProps: PropTypes.func
};

Layer.defaultProps = {
};

export default React.memo(Layer);