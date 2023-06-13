/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect, useContext } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { Layer as _Layer, useMap } from 'react-map-gl';
// 上下文管理器
import SourceContext from '../../contexts/SourceContext';

const Layer = (props) => {
    let { id, key, beforeId, layerProps, hoverCursor, setProps } = props;

    // 取得传递的地图实例
    const { current: map } = useMap();

    // 尝试取得来自Source组件的上下文信息
    const context = useContext(SourceContext);
    // 若来自Source的上下文信息中sourceId有效
    // 则强制覆盖当前图层参数中的source字段
    if (context?.sourceId) {
        layerProps = {
            ...layerProps,
            source: context.sourceId,
        };
    }

    // 处理要素鼠标悬停状态自定义cursor
    useEffect(() => {
        if (map && hoverCursor) {
            // 移入时修改cursor
            map.on('mouseenter', id, () => {
                map.getCanvas().style.cursor = hoverCursor;
            });
            // 移出时还原cursor
            map.on('mouseleave', id, () => {
                map.getCanvas().style.cursor = '';
            });
        }
    }, []);

    // 在当前Layer组件卸载时从map实例中移除当前组件id指向的图层
    useEffect(() => {
        return () => {
            try {
                if (map && map?.getLayer(id)) {
                    // 移除当前组件id指向的图层
                    map.removeLayer(id);
                }
            } catch (error) { }
        };
    }, []);

    return <_Layer id={id} key={key} beforeId={beforeId} {...layerProps} />;
};

Layer.propTypes = {
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
     * 当需要动态更新覆盖已有图层时，用于指定对应已有图层的id
     */
    beforeId: PropTypes.string,

    /**
     * 设置其他layer相关配置参数
     * 参考资料：https://maplibre.org/maplibre-style-spec/layers/
     */
    layerProps: PropTypes.object,

    /**
     * 针对当前图层设置鼠标悬停状态下的指针样式，同css属性中的cursor
     * 默认：null
     */
    hoverCursor: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

Layer.defaultProps = {};

export default React.memo(Layer);
