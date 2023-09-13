/* eslint-disable no-magic-numbers */
/* eslint-disable no-eval */
// 地图框架相关
import { useControl } from 'react-map-gl/maplibre';
// deck.gl相关
import { MapboxOverlay } from '@deck.gl/mapbox'
// 其他第三方辅助
import isUndefined from 'lodash/isUndefined';
import isNull from 'lodash/isNull';
import isObject from 'lodash/isObject';
import isString from 'lodash/isString';
import has from 'lodash/has';
import get from 'lodash/get';
import omitBy from 'lodash/omitBy';

const DeckGLOverlay = (props) => {
    const overlay = useControl(() => new MapboxOverlay(props));
    overlay.setProps(props);
    return null;
}

const parseDeckGet = (raw) => {

    if (isUndefined(raw)) {
        return null;
    }

    // 若当前输入为对象且具有func属性
    if (isObject(raw) && has(raw, 'func')) {
        try {
            return eval(raw.func)
        } catch (e) {
            console.error(e)
        }
    } else if (isString(raw)) {
        return (item) => {
            try {
                return get(item, raw);
            } catch (e) {
                console.error(e)
            }
            return null;
        }
    } else {
        return raw;
    }
    return null;
}

const omitNullAndUndefined = (raw) => {
    return omitBy(raw, (item) => isNull(item) || isUndefined(item));
}


const hex2RGB = (hex) => {
    let r = 0, g = 0, b = 0;

    if (hex.length === 4) {
        r = "0x" + hex[1] + hex[1];
        g = "0x" + hex[2] + hex[2];
        b = "0x" + hex[3] + hex[3];
    } else if (hex.length === 7) {
        r = "0x" + hex[1] + hex[2];
        g = "0x" + hex[3] + hex[4];
        b = "0x" + hex[5] + hex[6];
    }

    return [Number(r), Number(g), Number(b)];
}

export {
    DeckGLOverlay,
    parseDeckGet,
    omitNullAndUndefined,
    hex2RGB
};