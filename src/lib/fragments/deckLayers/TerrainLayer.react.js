/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
// deck.gl相关
import { TerrainLayer as _TerrainLayer } from '@deck.gl/geo-layers';
import { _GlobeView as GlobeView } from '@deck.gl/core';
// 自定义地图工具
import { DeckGLOverlay, omitNullAndUndefined } from '../../map_utils';
// 组件prop信息
import { propTypes, defaultProps } from '../../components/deckLayers/TerrainLayer.react';

const TerrainLayer = ({
    id,
    elevationData,
    texture,
    elevationDecoder,
    bounds,
    color,
    wireframe,
    material,
    setProps
}) => {

    let layerConfig = omitNullAndUndefined(
        {
            id: id,
            elevationData: elevationData,
            texture: texture,
            elevationDecoder: elevationDecoder,
            bounds: bounds,
            color: color,
            wireframe: wireframe,
            material: material,
            loadOptions: {
                terrain: {
                    skirtHeight: 25
                }
            }
        }
    )

    const terrainLayer = new _TerrainLayer(
        layerConfig
    );

    return <DeckGLOverlay
        layers={[terrainLayer]} />;
};


export default React.memo(TerrainLayer);

TerrainLayer.defaultProps = defaultProps;
TerrainLayer.propTypes = propTypes;