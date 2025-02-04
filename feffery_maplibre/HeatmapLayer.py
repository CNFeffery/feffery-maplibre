# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class HeatmapLayer(Component):
    """A HeatmapLayer component.


Keyword arguments:

- id (string; optional):
    用于唯一标识当前图层.

- key (string; optional):
    强制重绘当前组件时使用.

- data (list | string; optional):
    为当前图层设置数据源，当传入字符串时，代表数据源对应的url地址  默认：[].

- visible (boolean; default True):
    设置当前图层是否可见  默认：True.

- beforeId (string; optional):
    可选，设置当前图层插入已有图层位置之前所对应的图层id.

- opacity (number; default 1):
    设置当前图层透明度  默认：1.

- radiusPixels (number; default 30):
    热力点的像素半径  默认：30.

- colorRange (list; optional):
    热力点色彩方案数组  数组元素接受格式如[r, g, b, a]或[r, g, b].

- intensity (number; default 1):
    热力值强度系数，最终的热力权重值将会乘以该系数  默认：1.

- threshold (number; default 0.05):
    热力值阈值  默认：0.05.

- colorDomain (list of numbers; optional):
    限定热力值范围  格式如[最小值, 最大值].

- aggregation (a value equal to: 'SUM', 'MEAN'; default 'SUM'):
    设置针对每个像素点计算热力值使用到的聚合方式  可选的有'SUM'、'MEAN'  默认：'SUM'.

- weightsTextureSize (number; default 2048):
    调节热力渲染质地细致程度，更小的值意味着更快的渲染速度  默认：2048.

- debounceTimeout (number; default 500):
    调节当前热力图层随地图视角更新而随之更新，对应的防抖延时时长，单位：毫秒  默认：500.

- getPosition (dict; optional):
    控制热力点坐标驱动方式.

    `getPosition` is a string | dict with keys:

    - func (string; optional)

- getWeight (dict; optional):
    控制热力点权重驱动方式.

    `getWeight` is a number | string | dict with keys:

    - func (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'HeatmapLayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, data=Component.UNDEFINED, visible=Component.UNDEFINED, beforeId=Component.UNDEFINED, opacity=Component.UNDEFINED, radiusPixels=Component.UNDEFINED, colorRange=Component.UNDEFINED, intensity=Component.UNDEFINED, threshold=Component.UNDEFINED, colorDomain=Component.UNDEFINED, aggregation=Component.UNDEFINED, weightsTextureSize=Component.UNDEFINED, debounceTimeout=Component.UNDEFINED, getPosition=Component.UNDEFINED, getWeight=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'radiusPixels', 'colorRange', 'intensity', 'threshold', 'colorDomain', 'aggregation', 'weightsTextureSize', 'debounceTimeout', 'getPosition', 'getWeight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'radiusPixels', 'colorRange', 'intensity', 'threshold', 'colorDomain', 'aggregation', 'weightsTextureSize', 'debounceTimeout', 'getPosition', 'getWeight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(HeatmapLayer, self).__init__(**args)
