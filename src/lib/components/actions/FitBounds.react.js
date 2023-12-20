/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { useMap } from 'react-map-gl/maplibre';

const FitBounds = (props) => {
    let { mapActionConfig, abortPreviousAction, delay, delayAfterAction, setProps } = props;

    // 取得传递的地图实例
    const { current: map } = useMap();

    // 每次mapActionConfig有效时执行fitBounds()动作
    useEffect(() => {
        if (mapActionConfig) {
            // 拆分出bounds参数与其他参数
            let { bounds, ...rest } = mapActionConfig;
            if (abortPreviousAction) {
                if (delay) {
                    setTimeout(() => {
                        // 直接执行新动作
                        map.fitBounds(
                            bounds,
                            {
                                ...rest
                            }
                        )
                        setTimeout(() => {
                            setProps({ zoomAfterAction: map.getZoom() })
                        }, delayAfterAction)
                    }, delay)
                } else {
                    // 直接执行新动作
                    map.fitBounds(
                        bounds,
                        {
                            ...rest
                        }
                    )
                    setTimeout(() => {
                        setProps({ zoomAfterAction: map.getZoom() })
                    }, delayAfterAction)
                }
            } else if (!map.isMoving()) {
                // 否则则仅在地图静止时才执行新动作
                if (delay) {
                    setTimeout(() => {
                        // 直接执行新动作
                        map.fitBounds(
                            bounds,
                            {
                                ...rest
                            }
                        )
                        setTimeout(() => {
                            setProps({ zoomAfterAction: map.getZoom() })
                        }, delayAfterAction)
                    }, delay)
                } else {
                    // 直接执行新动作
                    map.fitBounds(
                        bounds,
                        {
                            ...rest
                        }
                    )
                    setTimeout(() => {
                        setProps({ zoomAfterAction: map.getZoom() })
                    }, delayAfterAction)
                }
            }
            // 重置参数
            setProps({ mapActionConfig: null })
        }
    }, [mapActionConfig])

    return <></>;
};

FitBounds.propTypes = {
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
         * 用于设置目标地图动作对应的地图视角坐标范围
         * 格式为[经度下限, 纬度下限, 经度上限, 纬度上限]
         * 默认：null
         */
        bounds: PropTypes.array,

        // 视角相关参数
        /**
         * 用于设置目标地图动作对应的缩放级别
         */
        zoom: PropTypes.number,

        /**
         * 用于设置目标地图动作对应的地图倾斜角度
         */
        pitch: PropTypes.number,

        /**
         * 用于设置目标地图动作对应的地图旋转角度
         */
        bearing: PropTypes.number,

        /**
         * 用于设置目标地图动作对应不同方向的像素留白大小
         */
        padding: PropTypes.exact({
            /**
             * 设置距离地图顶端的像素留白大小
             */
            top: PropTypes.number,

            /**
             * 设置距离地图底端的像素留白大小
             */
            bottom: PropTypes.number,

            /**
             * 设置距离地图左侧的像素留白大小
             */
            left: PropTypes.number,

            /**
             * 设置距离地图右侧的像素留白大小
             */
            right: PropTypes.number
        }),

        // 动画相关参数
        /**
         * 设置动画持续时长，单位：毫秒
         */
        duration: PropTypes.number,

        /**
         * 设置是否开启动画过渡效果
         */
        animate: PropTypes.bool,

        // 其他特殊参数
        /**
         * 设置是否开启线性动画效果，开启后动画效果类似EaseTo，关闭后类似FlyTo
         * 默认：false
         */
        linear: PropTypes.bool,

        /**
         * 用于设置向目标地图动作对应的bounds进行过渡时，最大允许的缩放层级
         */
        maxZoom: PropTypes.number
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

    // 监听类参数
    /**
     * 每次成功执行fitBounds动作后，监听最新的zoom级别
     */
    zoomAfterAction: PropTypes.number,

    /**
     * 设置在动作开始执行多少毫秒后，进行相关监听类参数的更新
     * 默认：500
     */
    delayAfterAction: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

FitBounds.defaultProps = {
    abortPreviousAction: true,
    delayAfterAction: 500
};

export default React.memo(FitBounds);
