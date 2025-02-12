# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class PanBy(Component):
    """A PanBy component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- key (string; optional):
    强制重绘当前组件时使用.

- mapActionConfig (dict; optional):
    用于设置要执行的地图动作参数，每次有效设置后会立即执行，且当前参数会在每次有效执行完成后被重置为空.

    `mapActionConfig` is a dict with keys:

    - offset (list of numbers; optional):
        用于设置目标地图动作对应水平、竖直方向上的相对像素偏移距离，格式如[水平像素偏移, 竖直像素偏移].

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
    _type = 'PanBy'
    MapActionConfig = TypedDict(
        "MapActionConfig",
            {
            "offset": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]],
            "duration": NotRequired[typing.Union[int, float, numbers.Number]],
            "animate": NotRequired[bool]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        mapActionConfig: typing.Optional["MapActionConfig"] = None,
        delay: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
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

        super(PanBy, self).__init__(**args)
