/* eslint-disable no-empty */
/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { useMap } from 'react-map-gl/maplibre';

const AddImages = ({ images = [], setProps }) => {

    // 取得传递的地图实例
    const { current: map } = useMap();

    useEffect(() => {
        if (map) {
            images = images || []
            for (let item of images) {
                try {
                    map.loadImage(
                        item.url,
                        (err, image) => {
                            map.addImage(item.id, image);
                        }
                    )
                } catch (e) {
                    console.log(item)
                    console.log(e.message)
                }
            }
            //  每次执行完成后重置images
            setProps({
                images: []
            })
        }
        // 每次执行完成后重置orders
        setProps({
            orders: [],
        });
    }, [images]);

    return <></>;
};

AddImages.propTypes = {
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
     * 设置最新一次需要向当前地图实例添加的静态图片资源信息
     * 默认：[]
     */
    images: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 当前图片资源id
             */
            id: PropTypes.string.isRequired,
            /**
             * 当前图片资源地址
             */
            url: PropTypes.string.isRequired,
        })
    ),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(AddImages);
