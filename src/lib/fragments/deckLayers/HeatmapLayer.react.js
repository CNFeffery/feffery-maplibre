/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
// deck.gl相关
import { HeatmapLayer as _HeatmapLayer } from '@deck.gl/aggregation-layers';
// 自定义地图工具
import { DeckGLOverlay, parseDeckGet, omitNullAndUndefined, hex2RGB } from '../../map_utils';
// 组件prop信息
import { propTypes, defaultProps } from '../../components/deckLayers/HeatmapLayer.react';


const HeatmapLayer = ({
    id,
    data,
    visible,
    beforeId,
    opacity,
    radiusPixels,
    colorRange,
    intensity,
    threshold,
    colorDomain,
    aggregation,
    weightsTextureSize,
    debounceTimeout,
    getPosition,
    getWeight,
    setProps
}) => {

    let layerConfig = omitNullAndUndefined(
        {
            id: id,
            data: data,
            visible: visible,
            beforeId: beforeId,
            opacity: opacity,
            radiusPixels: radiusPixels,
            colorRange: colorRange,
            intensity: intensity,
            threshold: threshold,
            colorDomain: colorDomain,
            aggregation: aggregation,
            weightsTextureSize: weightsTextureSize,
            debounceTimeout: debounceTimeout,
            getPosition: parseDeckGet(getPosition),
            getWeight: parseDeckGet(getWeight)
        }
    )

    const heatmapLayer = new _HeatmapLayer(
        layerConfig
    );

    return <DeckGLOverlay
        layers={[heatmapLayer]} />;
};


export default React.memo(HeatmapLayer);

HeatmapLayer.defaultProps = defaultProps;
HeatmapLayer.propTypes = propTypes;