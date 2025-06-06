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


class ZoomOut(Component):
    """A ZoomOut component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- key (string; optional):
    强制重绘当前组件时使用.

- mapActionConfig (dict; optional):
    用于设置要执行的地图动作参数，每次有效设置后会立即执行，且当前参数会在每次有效执行完成后被重置为空.

    `mapActionConfig` is a dict with keys:

    - duration (number; optional):
        设置动画持续时长，单位：毫秒.

    - animate (boolean; optional):
        设置是否开启动画过渡效果.

- delay (number; optional):
    设置动作延时，单位：毫秒.

- abortPreviousAction (boolean; default True):
    设置当上一段地图动作还未执行完成时，是否强制执行最新参数下的地图动作  默认：True."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'ZoomOut'
    MapActionConfig = TypedDict(
        "MapActionConfig",
            {
            "duration": NotRequired[NumberType],
            "animate": NotRequired[bool]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        mapActionConfig: typing.Optional["MapActionConfig"] = None,
        delay: typing.Optional[NumberType] = None,
        abortPreviousAction: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'mapActionConfig', 'delay', 'abortPreviousAction']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'mapActionConfig', 'delay', 'abortPreviousAction']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ZoomOut, self).__init__(**args)

setattr(ZoomOut, "__init__", _explicitize_args(ZoomOut.__init__))
