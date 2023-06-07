/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import {Source as _Source, useMap} from 'react-map-gl';
// 上下文管理器
import SourceContext from '../../contexts/SourceContext';

const Source = (props) => {
    const {id, children, key, sourceProps, setProps} = props;

    // 取得传递的地图实例
    const {current: map} = useMap();

    // 在当前Source组件卸载时从map实例中移除当前组件id指向的图层源
    useEffect(() => {
        return () => {
            if (map && map.getSource && map.getSource(id) && map.removeSource) {
                // 移除当前组件id指向的图层源
                map.removeSource(id);
            }
        };
    }, []);

    return (
        <SourceContext.Provider value={{sourceId: id}}>
            <_Source id={id} key={key} {...sourceProps}>
                {children}
            </_Source>
        </SourceContext.Provider>
    );
};

Source.propTypes = {
    // 基础参数
    /**
     * 必填，用于唯一标识当前图层源
     */
    id: PropTypes.string.isRequired,

    /**
     * 用于传入当前图层源内部对应的若干图层
     */
    children: PropTypes.node,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 设置其他source相关配置参数
     * 参考资料：https://maplibre.org/maplibre-style-spec/sources
     */
    sourceProps: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

Source.defaultProps = {};

export default React.memo(Source);
