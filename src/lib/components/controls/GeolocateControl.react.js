/* eslint-disable no-unused-vars */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 地图框架相关
import { GeolocateControl as _GeolocateControl } from 'react-map-gl/maplibre';


const GeolocateControl = (props) => {
    const {
        id,
        key,
        style,
        position,
        positionOptions,
        showUserLocation,
        showAccuracyCircle,
        showUserHeading,
        trackUserLocation,
        setProps
    } = props;

    return (
        <_GeolocateControl id={id}
            key={key}
            style={style}
            position={position}
            positionOptions={positionOptions}
            showUserLocation={showUserLocation}
            showAccuracyCircle={showAccuracyCircle}
            showUserHeading={showUserHeading}
            trackUserLocation={trackUserLocation}
            onGeolocate={(e) => console.log('onGeolocate: ', e)}
        />
    );
}

GeolocateControl.propTypes = {
    // 基础参数
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 用于设置当前控件容器的css样式
     */
    style: PropTypes.object,

    /**
     * 设置当前定位控件显示方位
     * 可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
     * 默认：'bottom-right'
     */
    position: PropTypes.oneOf(['top-right', 'top-left', 'bottom-right', 'bottom-left']),

    /**
     * 配置定位相关行为参数
     */
    positionOptions: PropTypes.exact({
        /**
         * 定位信息缓存时长，单位：毫秒
         * 默认：0，即不缓存
         */
        maximumAge: PropTypes.number,

        /**
         * 定位请求超时时长，单位：毫秒
         * 默认：6000
         */
        timeout: PropTypes.number,

        /**
         * 是否开启高精度定位
         * 默认：false
         */
        enableHighAccuracy: PropTypes.bool
    }),

    /**
     * 是否展示定位点标记
     * 默认：true
     */
    showUserLocation: PropTypes.bool,

    /**
     * 是否展示定位范围95%置信区间圆圈，当showUserLocation为false时会自动禁用
     * 默认：true
     */
    showAccuracyCircle: PropTypes.bool,

    /**
     * 是否展示定位点方向标记，仅在trackUserLocation为true时可用
     * 默认：false
     */
    showUserHeading: PropTypes.bool,

    /**
     * 是否持续监听用户位置
     * 默认：false
     */
    trackUserLocation: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
    */
    setProps: PropTypes.func
};

GeolocateControl.defaultProps = {
    position: 'bottom-right',
    showUserLocation: true,
    showAccuracyCircle: true,
    trackUserLocation: false,
    showUserHeading: false
};

export default React.memo(GeolocateControl);