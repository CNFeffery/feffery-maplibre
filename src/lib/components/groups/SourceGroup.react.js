/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';

const SourceGroup = (props) => {
    const {id, children, key, setProps} = props;

    return <>{children}</>;
};

SourceGroup.propTypes = {
    // 基础参数
    /**
     * 用于唯一标识当前组件
     */
    id: PropTypes.string,

    /**
     * 用于传入当前图层源组内部对应的若干图层源组件
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

SourceGroup.defaultProps = {};

export default React.memo(SourceGroup);
