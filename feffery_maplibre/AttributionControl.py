# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AttributionControl(Component):
    """An AttributionControl component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- customAttribution (string; optional):
    设置标注属性信息.

- key (string; optional):
    强制重绘当前组件时使用.

- position (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'top-right'):
    设置当前属性控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'top-right'.

- style (dict; optional):
    用于设置当前控件容器的css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'AttributionControl'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, customAttribution=Component.UNDEFINED, position=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'customAttribution', 'key', 'position', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'customAttribution', 'key', 'position', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AttributionControl, self).__init__(**args)
