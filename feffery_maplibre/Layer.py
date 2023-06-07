# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Layer(Component):
    """A Layer component.


Keyword arguments:

- id (string; required):
    必填，用于唯一标识当前矢量切片图层.

- beforeId (string; optional):
    当需要动态更新覆盖已有矢量切片图层时，用于指定对应已有矢量切片图层的id.

- hoverCursor (string; optional):
    针对当前图层设置鼠标悬停状态下的指针样式，同css属性中的cursor  默认：None.

- key (string; optional):
    强制重绘当前组件时使用.

- layerProps (dict; optional):
    设置其他layer相关配置参数
    参考资料：https://maplibre.org/maplibre-style-spec/layers/."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Layer'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, key=Component.UNDEFINED, beforeId=Component.UNDEFINED, layerProps=Component.UNDEFINED, hoverCursor=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'beforeId', 'hoverCursor', 'key', 'layerProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'beforeId', 'hoverCursor', 'key', 'layerProps']
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
