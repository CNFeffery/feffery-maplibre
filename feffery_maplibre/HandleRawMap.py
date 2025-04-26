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


class HandleRawMap(Component):
    """A HandleRawMap component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- key (string; optional):
    强制重绘当前组件时使用.

- jsString (string; optional):
    设置要针对当前地图实例中的map对象执行的javascript代码字符串  每次新的执行完成后会自动重置为None
    默认：None."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'HandleRawMap'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        jsString: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'jsString']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'jsString']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(HandleRawMap, self).__init__(**args)

setattr(HandleRawMap, "__init__", _explicitize_args(HandleRawMap.__init__))
