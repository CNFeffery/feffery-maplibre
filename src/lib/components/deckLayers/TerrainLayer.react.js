/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyTerrainLayer = React.lazy(() => import(/* webpackChunkName: "deck_gl_layers" */ '../../fragments/deckLayers/TerrainLayer.react'));

const TerrainLayer = ({
    id,
    elevationData,
    texture,
    elevationDecoder = {
        rScaler: 6553.6,
        gScaler: 25.6,
        bScaler: 0.1,
        offset: -10000
    },
    bounds,
    color = [255, 255, 255],
    wireframe = false,
    material = true,
    setProps
}) => {
    return (
        <Suspense fallback={null}>
            <LazyTerrainLayer {
                ...{
                    id,
                    elevationData,
                    texture,
                    elevationDecoder,
                    bounds,
                    color,
                    wireframe,
                    material,
                    setProps
                }
            } />
        </Suspense>
    );
}

TerrainLayer.propTypes = {
    // 基础参数
    /**
     * 用于唯一标识当前图层
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 必填，设置高程地图服务地址
     */
    elevationData: PropTypes.string.isRequired,

    /**
     * 设置随高程被拉伸的瓦片地图服务地址
     */
    texture: PropTypes.string,

    /**
     * 自定义rgb高程数据解码规则，默认为mapbox-rgb规则
     */
    elevationDecoder: PropTypes.exact({
        /**
         * 红色通道系数
         */
        rScaler: PropTypes.number,

        /**
         * 绿色通道系数
         */
        gScaler: PropTypes.number,

        /**
         * 蓝色通道系数
         */
        bScaler: PropTypes.number,

        /**
         * 偏移系数
         */
        offset: PropTypes.number
    }),

    /**
     * 设置当前地形图层作用范围
     * 格式为：[min_x, min_y, max_x, max_y]
     */
    bounds: PropTypes.arrayOf(PropTypes.number),

    /**
     * 当参数texture为空时，用于手动设置地形渲染颜色
     * 默认：[255, 255, 255]
     */
    color: PropTypes.arrayOf(PropTypes.number),

    /**
     * 设置是否渲染地形骨架线框
     * 默认：false
     */
    wireframe: PropTypes.bool,

    /**
     * 设置是否开启材质效果
     * 默认：true
     */
    material: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(TerrainLayer);

export const propTypes = TerrainLayer.propTypes;
export const defaultProps = TerrainLayer.defaultProps;