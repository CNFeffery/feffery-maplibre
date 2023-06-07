/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';

const LayerGroup = (props) => {
    const {id, children, key, setProps} = props;

    return <>{children}</>;
};

LayerGroup.propTypes = {
    // 基础参数
    /**
     * 用于唯一标识当前组件
     */
    id: PropTypes.string,

    /**
     * 用于传入当前图层组内部对应的若干图层组件
     */
    children: PropTypes.node,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

LayerGroup.defaultProps = {};

export default React.memo(LayerGroup);
