/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import {Source as _Source} from 'react-map-gl';
// 上下文管理器
import SourceContext from '../../contexts/SourceContext';

const Source = (props) => {
    const {id, children, key, sourceProps, setProps} = props;

    return (
        <SourceContext.Provider value={{sourceId: id}}>
            <_Source id={id} key={key} type={'vector'} {...sourceProps}>
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
     * 用于传入当前矢量切片图层源内部对应的若干矢量切片图层
     */
    children: PropTypes.node,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 设置其他source相关配置参数
     * 参考资料：https://maplibre.org/maplibre-style-spec/sources/#vector
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
