# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class ScaleControl(Component):
    """A ScaleControl component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- key (string; optional):
    强制重绘当前组件时使用.

- position (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'bottom-left'):
    设置当前比例尺控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'bottom-left'.

- maxWidth (number; default 100):
    设置当前比例尺控件最大像素宽度  默认：100."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'ScaleControl'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        position: typing.Optional[Literal["top-right", "top-left", "bottom-right", "bottom-left"]] = None,
        maxWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'position', 'maxWidth']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'position', 'maxWidth']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ScaleControl, self).__init__(**args)
