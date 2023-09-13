/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
// deck.gl相关
import { GeoJsonLayer as _GeoJsonLayer } from '@deck.gl/layers';
// 自定义地图工具
import { DeckGLOverlay, parseDeckGet, omitNullAndUndefined, hex2RGB } from '../../map_utils';
// 组件prop信息
import { propTypes, defaultProps } from '../../components/deckLayers/GeoJsonLayer.react';
// 其他第三方辅助
import { useRequest } from 'ahooks';


const GeoJsonLayer = (props) => {
    let {
        id,
        data,
        visible,
        opacity,
        pickable,
        highlightColor,
        autoHighlight,
        tooltipRenderer,
        pointType,
        filled,
        stroked,
        lineWidthUnits,
        lineWidthScale,
        lineWidthMinPixels,
        lineWidthMaxPixels,
        lineBillboard,
        extruded,
        wireframe,
        elevationScale,
        pointRadiusUnits,
        pointRadiusScale,
        pointRadiusMinPixels,
        pointRadiusMaxPixels,
        pointBillboard,
        getFillColor,
        getLineColor,
        getLineWidth,
        getElevation,
        getPointRadius,
        debounceWait,
        setProps
    } = props;

    const { run: onDebounceHover } = useRequest(
        (e) => {
            setProps({
                hoverEvent: {
                    coordinate: e.coordinate,
                    devicePixel: e.devicePixel,
                    pixel: e.pixel,
                    layerId: e.layer.id,
                    data: e.object,
                    index: e.index,
                    timestamp: Date.now()
                }
            })
        },
        {
            debounceWait: debounceWait,
            manual: true
        }
    )

    const { run: onDebounceClick } = useRequest(
        (e) => {
            setProps({
                clickEvent: {
                    coordinate: e.coordinate,
                    devicePixel: e.devicePixel,
                    pixel: e.pixel,
                    layerId: e.layer.id,
                    data: e.object,
                    index: e.index,
                    timestamp: Date.now()
                }
            })
        },
        {
            debounceWait: debounceWait,
            manual: true
        }
    )

    let layerConfig = omitNullAndUndefined(
        {
            id,
            data,
            visible,
            opacity,
            pickable,
            highlightColor,
            autoHighlight,
            pointType,
            filled,
            stroked,
            lineWidthUnits,
            lineWidthScale,
            lineWidthMinPixels,
            lineWidthMaxPixels,
            lineBillboard,
            extruded,
            wireframe,
            elevationScale,
            pointRadiusUnits,
            pointRadiusScale,
            pointRadiusMinPixels,
            pointRadiusMaxPixels,
            pointBillboard,
            getFillColor: parseDeckGet(getFillColor),
            getLineColor: parseDeckGet(getLineColor),
            getLineWidth: parseDeckGet(getLineWidth),
            getElevation: parseDeckGet(getElevation),
            getPointRadius: parseDeckGet(getPointRadius),
            onHover: onDebounceHover,
            onClick: onDebounceClick
        }
    )

    const geoJsonLayer = new _GeoJsonLayer(
        layerConfig
    );

    // 根据tooltipRenderer参数生成getTooltip函数
    let getTooltip = null;
    try {
        getTooltip = eval(tooltipRenderer);
    } catch (e) {
        console.error(e);
    }

    return <DeckGLOverlay
        getTooltip={getTooltip}
        layers={[geoJsonLayer]} />;
};


export default React.memo(GeoJsonLayer);

GeoJsonLayer.defaultProps = defaultProps;
GeoJsonLayer.propTypes = propTypes;