/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';

const Fragment = (props) => (<>{props.children}</>);

Fragment.propTypes = {
    // 基础参数
    /**
     * 必填，用于唯一标识当前组件
     */
    id: PropTypes.string,

    /**
     * 用于传入内部组件
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

export default React.memo(Fragment);
