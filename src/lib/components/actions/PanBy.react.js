/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { useMap } from 'react-map-gl/maplibre';

const PanBy = (props) => {
    let { mapActionConfig, abortPreviousAction, delay, setProps } = props;

    // 取得传递的地图实例
    const { current: map } = useMap();

    // 每次mapActionConfig有效时执行panBy()动作
    useEffect(() => {
        if (mapActionConfig) {
            // 拆分出offset参数与其他参数
            let { offset, ...rest } = mapActionConfig;
            if (abortPreviousAction) {
                if (delay) {
                    // 延时执行
                    setTimeout(() => {
                        // 直接执行新动作
                        map.panBy(
                            offset,
                            {
                                ...rest
                            }
                        )
                    }, delay)
                } else {
                    // 直接执行新动作
                    map.panBy(
                        offset,
                        {
                            ...rest
                        }
                    )
                }
            } else if (!map.isMoving()) {
                // 否则则仅在地图静止时才执行新动作
                if (delay) {
                    // 延时执行
                    setTimeout(() => {
                        map.panBy(
                            offset,
                            {
                                ...rest
                            }
                        )
                    }, delay)
                } else {
                    map.panBy(
                        offset,
                        {
                            ...rest
                        }
                    )
                }
            }
            // 重置参数
            setProps({ mapActionConfig: null })
        }
    }, [mapActionConfig])

    return <></>;
};

PanBy.propTypes = {
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
     * 用于设置要执行的地图动作参数，每次有效设置后会立即执行，且当前参数会在每次有效执行完成后被重置为空
     */
    mapActionConfig: PropTypes.exact({
        /**
         * 用于设置目标地图动作对应水平、竖直方向上的相对像素偏移距离，格式如[水平像素偏移, 竖直像素偏移]
         */
        offset: PropTypes.arrayOf(PropTypes.number),

        // 动画相关参数
        /**
         * 设置动画持续时长，单位：毫秒
         */
        duration: PropTypes.number,

        /**
         * 设置是否开启动画过渡效果
         */
        animate: PropTypes.bool
    }),

    /**
     * 设置动作延时，单位：毫秒
     */
    delay: PropTypes.number,

    /**
     * 设置当上一段地图动作还未执行完成时，是否强制执行最新参数下的地图动作
     * 默认：true
     */
    abortPreviousAction: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

PanBy.defaultProps = {
    abortPreviousAction: true
};

export default React.memo(PanBy);
