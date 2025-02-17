# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Layer(Component):
    """A Layer component.


Keyword arguments:

- id (string; required):
    必填，用于唯一标识当前图层.

- key (string; optional):
    强制重绘当前组件时使用.

- layerId (string; optional):
    设置当前图层id，优先级高于id.

- beforeId (string; optional):
    当需要动态更新覆盖已有图层时，用于指定对应已有图层的id.

- layerProps (dict; optional):
    设置其他layer相关配置参数
    参考资料：https://maplibre.org/maplibre-style-spec/layers/.

- hoverCursor (string; optional):
    针对当前图层设置鼠标悬停状态下的指针样式，同css属性中的cursor  默认：None."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Layer'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        layerId: typing.Optional[str] = None,
        beforeId: typing.Optional[str] = None,
        layerProps: typing.Optional[dict] = None,
        hoverCursor: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'layerId', 'beforeId', 'layerProps', 'hoverCursor']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'layerId', 'beforeId', 'layerProps', 'hoverCursor']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Layer, self).__init__(**args)
