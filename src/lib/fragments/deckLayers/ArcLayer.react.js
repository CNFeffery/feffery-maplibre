/* eslint-disable no-unused-vars */
/* eslint-disable no-eval */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
// deck.gl相关
import { ArcLayer as _ArcLayer } from '@deck.gl/layers';
// 自定义地图工具
import { DeckGLOverlay, parseDeckGet, omitNullAndUndefined } from '../../map_utils';
// 组件prop信息
import { propTypes, defaultProps } from '../../components/deckLayers/ArcLayer.react';
// 其他第三方辅助
import { useRequest } from 'ahooks';


const ArcLayer = (props) => {
    let {
        id,
        data,
        visible,
        opacity,
        pickable,
        highlightColor,
        autoHighlight,
        tooltipRenderer,
        greatCircle,
        numSegments,
        widthUnits,
        widthScale,
        widthMinPixels,
        widthMaxPixels,
        getSourcePosition,
        getTargetPosition,
        getSourceColor,
        getTargetColor,
        getWidth,
        getHeight,
        getTilt,
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
            id: id,
            data: data,
            visible: visible,
            opacity: opacity,
            pickable: pickable,
            highlightColor: highlightColor,
            autoHighlight: autoHighlight,
            greatCircle: greatCircle,
            numSegments: numSegments,
            widthUnits: widthUnits,
            widthScale: widthScale,
            widthMinPixels: widthMinPixels,
            widthMaxPixels: widthMaxPixels,
            getSourcePosition: parseDeckGet(getSourcePosition),
            getTargetPosition: parseDeckGet(getTargetPosition),
            getSourceColor: parseDeckGet(getSourceColor),
            getTargetColor: parseDeckGet(getTargetColor),
            getWidth: parseDeckGet(getWidth),
            getHeight: parseDeckGet(getHeight),
            getTilt: parseDeckGet(getTilt),
            onHover: onDebounceHover,
            onClick: onDebounceClick
        }
    )

    const arcLayer = new _ArcLayer(
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
        layers={[arcLayer]} />;
};


export default React.memo(ArcLayer);

ArcLayer.defaultProps = defaultProps;
ArcLayer.propTypes = propTypes;