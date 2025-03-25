# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class TerrainLayer(Component):
    """A TerrainLayer component.


Keyword arguments:

- id (string; optional):
    用于唯一标识当前图层.

- key (string; optional):
    强制重绘当前组件时使用.

- elevationData (string; required):
    必填，设置高程地图服务地址.

- texture (string; optional):
    设置随高程被拉伸的瓦片地图服务地址.

- elevationDecoder (dict; default {    rScaler: 6553.6,    gScaler: 25.6,    bScaler: 0.1,    offset: -10000}):
    自定义rgb高程数据解码规则，默认为mapbox-rgb规则.

    `elevationDecoder` is a dict with keys:

    - rScaler (number; optional):
        红色通道系数.

    - gScaler (number; optional):
        绿色通道系数.

    - bScaler (number; optional):
        蓝色通道系数.

    - offset (number; optional):
        偏移系数.

- bounds (list of numbers; optional):
    设置当前地形图层作用范围  格式为：[min_x, min_y, max_x, max_y].

- color (list of numbers; default [255, 255, 255]):
    当参数texture为空时，用于手动设置地形渲染颜色  默认：[255, 255, 255].

- wireframe (boolean; default False):
    设置是否渲染地形骨架线框  默认：False.

- material (boolean; default True):
    设置是否开启材质效果  默认：True."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'TerrainLayer'
    ElevationDecoder = TypedDict(
        "ElevationDecoder",
            {
            "rScaler": NotRequired[typing.Union[int, float, numbers.Number]],
            "gScaler": NotRequired[typing.Union[int, float, numbers.Number]],
            "bScaler": NotRequired[typing.Union[int, float, numbers.Number]],
            "offset": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        elevationData: typing.Optional[str] = None,
        texture: typing.Optional[str] = None,
        elevationDecoder: typing.Optional["ElevationDecoder"] = None,
        bounds: typing.Optional[typing.Sequence[typing.Union[int, float, numbers.Number]]] = None,
        color: typing.Optional[typing.Sequence[typing.Union[int, float, numbers.Number]]] = None,
        wireframe: typing.Optional[bool] = None,
        material: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'elevationData', 'texture', 'elevationDecoder', 'bounds', 'color', 'wireframe', 'material']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'elevationData', 'texture', 'elevationDecoder', 'bounds', 'color', 'wireframe', 'material']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['elevationData']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(TerrainLayer, self).__init__(**args)
