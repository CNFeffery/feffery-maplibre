# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ScaleControl(Component):
    """A ScaleControl component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- key (string; optional):
    强制重绘当前组件时使用.

- maxWidth (number; default 100):
    设置当前比例尺控件最大像素宽度  默认：100.

- position (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'bottom-left'):
    设置当前比例尺控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'bottom-left'.

- style (dict; optional):
    用于设置当前地图容器的css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'ScaleControl'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, position=Component.UNDEFINED, maxWidth=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'maxWidth', 'position', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'maxWidth', 'position', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ScaleControl, self).__init__(**args)
