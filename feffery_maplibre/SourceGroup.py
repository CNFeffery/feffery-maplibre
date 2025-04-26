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


class SourceGroup(Component):
    """A SourceGroup component.


Keyword arguments:

- id (string; optional):
    用于唯一标识当前组件.

- children (a list of or a singular dash component, string or number; optional):
    用于传入当前图层源组内部对应的若干图层源组件.

- key (string; optional):
    强制重绘当前组件时使用."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'SourceGroup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'children', 'key']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'key']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SourceGroup, self).__init__(children=children, **args)

setattr(SourceGroup, "__init__", _explicitize_args(SourceGroup.__init__))
