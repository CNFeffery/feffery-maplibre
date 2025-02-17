# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Stop(Component):
    """A Stop component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- key (string; optional):
    强制重绘当前组件时使用.

- execute (boolean; default False):
    是否执行停止动作，默认为False，每次设置为True并成功停止动画后，会被重置为False.

- delay (number; optional):
    设置动作延时，单位：毫秒."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Stop'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        execute: typing.Optional[bool] = None,
        delay: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'execute', 'delay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'execute', 'delay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Stop, self).__init__(**args)
