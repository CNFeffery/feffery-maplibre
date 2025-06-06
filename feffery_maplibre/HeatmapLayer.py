# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


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
    GetPosition = TypedDict(
        "GetPosition",
            {
            "func": NotRequired[str]
        }
    )

    GetWeight = TypedDict(
        "GetWeight",
            {
            "func": NotRequired[str]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        data: typing.Optional[typing.Union[typing.Sequence, str]] = None,
        visible: typing.Optional[bool] = None,
        beforeId: typing.Optional[str] = None,
        opacity: typing.Optional[NumberType] = None,
        radiusPixels: typing.Optional[NumberType] = None,
        colorRange: typing.Optional[typing.Sequence] = None,
        intensity: typing.Optional[NumberType] = None,
        threshold: typing.Optional[NumberType] = None,
        colorDomain: typing.Optional[typing.Sequence[NumberType]] = None,
        aggregation: typing.Optional[Literal["SUM", "MEAN"]] = None,
        weightsTextureSize: typing.Optional[NumberType] = None,
        debounceTimeout: typing.Optional[NumberType] = None,
        getPosition: typing.Optional[typing.Union[str, "GetPosition"]] = None,
        getWeight: typing.Optional[typing.Union[NumberType, str, "GetWeight"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'radiusPixels', 'colorRange', 'intensity', 'threshold', 'colorDomain', 'aggregation', 'weightsTextureSize', 'debounceTimeout', 'getPosition', 'getWeight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'radiusPixels', 'colorRange', 'intensity', 'threshold', 'colorDomain', 'aggregation', 'weightsTextureSize', 'debounceTimeout', 'getPosition', 'getWeight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(HeatmapLayer, self).__init__(**args)

setattr(HeatmapLayer, "__init__", _explicitize_args(HeatmapLayer.__init__))
