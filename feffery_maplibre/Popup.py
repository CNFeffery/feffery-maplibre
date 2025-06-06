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


class Popup(Component):
    """A Popup component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- children (a list of or a singular dash component, string or number; optional):
    设置内部元素，用于代替缺省的标记图标.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于设置当前弹出卡片的css类名.

- latitude (number; required):
    必填，设置当前标记对应位置纬度.

- longitude (number; required):
    必填，设置当前标记对应位置经度.

- anchor (a value equal to: 'center', 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right'; optional):
    当前弹出卡片相对坐标点的方位
    可选的有'center'、'top'、'bottom'、'left'、'right'、'top-left'、'top-right'、'bottom-left'、'bottom-right'
    默认：'center'.

- maxWidth (string; default '240px'):
    设置当前弹出卡片的最大宽度  默认：'240px'.

- closeButton (boolean; default True):
    是否显示关闭按钮  默认：True.

- closeOnMove (boolean; default False):
    地图移动时是否触发关闭  默认：False.

- closeOnClick (boolean; default True):
    点击地图其他位置是否触发关闭  默认：True.

- offset (list of numbers; optional):
    设置当前弹出卡片在水平和竖直方向上需要进行的像素偏移  格式如：[水平像素偏移, 竖直像素偏移]."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Popup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        latitude: typing.Optional[NumberType] = None,
        longitude: typing.Optional[NumberType] = None,
        anchor: typing.Optional[Literal["center", "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right"]] = None,
        maxWidth: typing.Optional[str] = None,
        closeButton: typing.Optional[bool] = None,
        closeOnMove: typing.Optional[bool] = None,
        closeOnClick: typing.Optional[bool] = None,
        offset: typing.Optional[typing.Sequence[NumberType]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'children', 'key', 'style', 'className', 'latitude', 'longitude', 'anchor', 'maxWidth', 'closeButton', 'closeOnMove', 'closeOnClick', 'offset']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'key', 'style', 'className', 'latitude', 'longitude', 'anchor', 'maxWidth', 'closeButton', 'closeOnMove', 'closeOnClick', 'offset']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['latitude', 'longitude']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Popup, self).__init__(children=children, **args)

setattr(Popup, "__init__", _explicitize_args(Popup.__init__))
