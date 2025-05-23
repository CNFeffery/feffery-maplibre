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


class Marker(Component):
    """A Marker component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- children (a list of or a singular dash component, string or number; optional):
    设置内部元素，用于代替缺省的标记图标.

- key (string; optional):
    强制重绘当前组件时使用.

- anchor (a value equal to: 'center', 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right'; default 'center'):
    当前标记坐标点相对标记内容的方位
    可选的有'center'、'top'、'bottom'、'left'、'right'、'top-left'、'top-right'、'bottom-left'、'bottom-right'
    默认：'center'.

- color (string; default '#3FB1CE'):
    当前标记颜色  默认：'#3FB1CE'.

- draggable (boolean; default False):
    当前标记是否可自由拖动  默认：False.

- latitude (number; required):
    必填，设置当前标记对应位置纬度.

- longitude (number; required):
    必填，设置当前标记对应位置经度.

- offset (list of numbers; optional):
    设置当前标记位置在水平、竖直方向上的像素偏移.

- pitchAlignment (a value equal to: 'map', 'viewport', 'auto'; default 'auto'):
    设置当前标记倾斜角度的对齐方式，可选的有'map'、'viewport'、'auto'  默认：'auto'.

- rotation (number; default 0):
    设置当前标记的旋转角度  默认：0.

- rotationAlignment (a value equal to: 'map', 'viewport', 'auto'; default 'auto'):
    设置当前标记旋转角度的对齐方式，可选的有'map'、'viewport'、'auto'  默认：'auto'.

- scale (number; default 1):
    设置当前标记的缩放倍数  默认：1.

- nClicks (number; default 0):
    监听当前标记累计被点击次数.

- debounceWait (number; default 200):
    设置针对当前地图容器的防抖延时，单位：毫秒  默认：200.

- longitudeDebounce (number; optional):
    防抖监听参数，用于监听当前地图中心点经度.

- latitudeDebounce (number; optional):
    防抖监听参数，用于监听当前地图中心点纬度."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Marker'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        anchor: typing.Optional[Literal["center", "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right"]] = None,
        color: typing.Optional[str] = None,
        draggable: typing.Optional[bool] = None,
        latitude: typing.Optional[NumberType] = None,
        longitude: typing.Optional[NumberType] = None,
        offset: typing.Optional[typing.Sequence[NumberType]] = None,
        pitchAlignment: typing.Optional[Literal["map", "viewport", "auto"]] = None,
        rotation: typing.Optional[NumberType] = None,
        rotationAlignment: typing.Optional[Literal["map", "viewport", "auto"]] = None,
        scale: typing.Optional[NumberType] = None,
        nClicks: typing.Optional[NumberType] = None,
        debounceWait: typing.Optional[NumberType] = None,
        longitudeDebounce: typing.Optional[NumberType] = None,
        latitudeDebounce: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'children', 'key', 'style', 'anchor', 'color', 'draggable', 'latitude', 'longitude', 'offset', 'pitchAlignment', 'rotation', 'rotationAlignment', 'scale', 'nClicks', 'debounceWait', 'longitudeDebounce', 'latitudeDebounce']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'key', 'style', 'anchor', 'color', 'draggable', 'latitude', 'longitude', 'offset', 'pitchAlignment', 'rotation', 'rotationAlignment', 'scale', 'nClicks', 'debounceWait', 'longitudeDebounce', 'latitudeDebounce']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['latitude', 'longitude']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Marker, self).__init__(children=children, **args)

setattr(Marker, "__init__", _explicitize_args(Marker.__init__))
