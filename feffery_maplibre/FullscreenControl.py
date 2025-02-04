# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FullscreenControl(Component):
    """A FullscreenControl component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于设置当前控件容器的css样式.

- position (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'top-right'):
    设置当前全屏控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'top-right'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'FullscreenControl'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, position=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'position']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'position']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FullscreenControl, self).__init__(**args)
