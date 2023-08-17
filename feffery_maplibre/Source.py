# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Source(Component):
    """A Source component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于传入当前图层源内部对应的若干图层.

- id (string; required):
    必填，用于唯一标识当前图层源.

- key (string; optional):
    强制重绘当前组件时使用.

- sourceId (string; optional):
    设置当前图层源id，优先级高于id.

- sourceProps (dict; optional):
    设置其他source相关配置参数
    参考资料：https://maplibre.org/maplibre-style-spec/sources."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Source'
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, key=Component.UNDEFINED, sourceId=Component.UNDEFINED, sourceProps=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'key', 'sourceId', 'sourceProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'key', 'sourceId', 'sourceProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Source, self).__init__(children=children, **args)
