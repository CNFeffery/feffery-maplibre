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


class AttributionControl(Component):
    """An AttributionControl component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- key (string; optional):
    强制重绘当前组件时使用.

- customAttribution (string; optional):
    设置标注属性信息.

- position (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'bottom-right'):
    设置当前属性控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'bottom-right'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'AttributionControl'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        customAttribution: typing.Optional[str] = None,
        position: typing.Optional[Literal["top-right", "top-left", "bottom-right", "bottom-left"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'customAttribution', 'position']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'customAttribution', 'position']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AttributionControl, self).__init__(**args)

setattr(AttributionControl, "__init__", _explicitize_args(AttributionControl.__init__))
