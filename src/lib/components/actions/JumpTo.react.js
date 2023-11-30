/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { useMap } from 'react-map-gl/maplibre';

const JumpTo = (props) => {
    let { mapActionConfig, delay, setProps } = props;

    // 取得传递的地图实例
    const { current: map } = useMap();

    // 每次mapActionConfig有效时执行jumpTo()动作
    useEffect(() => {
        if (mapActionConfig) {
            if (delay) {
                // 延时执行
                setTimeout(() => {
                    // 直接执行新动作
                    map.easeTo(
                        {
                            ...mapActionConfig
                        }
                    )
                }, delay)
            } else {
                // 直接执行新动作
                map.easeTo(
                    {
                        ...mapActionConfig
                    }
                )
            }
            // 重置参数
            setProps({ mapActionConfig: null })
        }
    }, [mapActionConfig])

    return <></>;
};

JumpTo.propTypes = {
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
        // 视角相关参数
        /**
         * 用于设置目标地图动作对应的中心坐标
         * 格式如[中心经度, 中心纬度]
         */
        center: PropTypes.arrayOf(PropTypes.number),

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
        })
    }),

    /**
 * 设置动作延时，单位：毫秒
 */
    delay: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

JumpTo.defaultProps = {
};

export default React.memo(JumpTo);
