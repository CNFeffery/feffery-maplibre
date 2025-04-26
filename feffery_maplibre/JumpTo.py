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


class JumpTo(Component):
    """A JumpTo component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- key (string; optional):
    强制重绘当前组件时使用.

- mapActionConfig (dict; optional):
    用于设置要执行的地图动作参数，每次有效设置后会立即执行，且当前参数会在每次有效执行完成后被重置为空.

    `mapActionConfig` is a dict with keys:

    - center (list of numbers; optional):
        用于设置目标地图动作对应的中心坐标  格式如[中心经度, 中心纬度].

    - zoom (number; optional):
        用于设置目标地图动作对应的缩放级别.

    - pitch (number; optional):
        用于设置目标地图动作对应的地图倾斜角度.

    - bearing (number; optional):
        用于设置目标地图动作对应的地图旋转角度.

    - padding (dict; optional):
        用于设置目标地图动作对应不同方向的像素留白大小.

        `padding` is a dict with keys:

        - top (number; optional):
            设置距离地图顶端的像素留白大小.

        - bottom (number; optional):
            设置距离地图底端的像素留白大小.

        - left (number; optional):
            设置距离地图左侧的像素留白大小.

        - right (number; optional):
            设置距离地图右侧的像素留白大小.

- delay (number; optional):
    设置动作延时，单位：毫秒."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'JumpTo'
    MapActionConfigPadding = TypedDict(
        "MapActionConfigPadding",
            {
            "top": NotRequired[NumberType],
            "bottom": NotRequired[NumberType],
            "left": NotRequired[NumberType],
            "right": NotRequired[NumberType]
        }
    )

    MapActionConfig = TypedDict(
        "MapActionConfig",
            {
            "center": NotRequired[typing.Sequence[NumberType]],
            "zoom": NotRequired[NumberType],
            "pitch": NotRequired[NumberType],
            "bearing": NotRequired[NumberType],
            "padding": NotRequired["MapActionConfigPadding"]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        mapActionConfig: typing.Optional["MapActionConfig"] = None,
        delay: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'mapActionConfig', 'delay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'mapActionConfig', 'delay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(JumpTo, self).__init__(**args)

setattr(JumpTo, "__init__", _explicitize_args(JumpTo.__init__))
