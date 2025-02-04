# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NavigationControl(Component):
    """A NavigationControl component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于设置当前控件容器的css样式.

- position (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'top-right'):
    设置当前导航控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'top-right'.

- showCompass (boolean; default True):
    设置导航控件中是否显示指南针按钮  默认：True.

- showZoom (boolean; default True):
    设置导航控件中是否显示缩放按钮  默认：True.

- visualizePitch (boolean; default False):
    设置导航控件中的指南针图标是否展示地图倾斜状态  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'NavigationControl'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, position=Component.UNDEFINED, showCompass=Component.UNDEFINED, showZoom=Component.UNDEFINED, visualizePitch=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'position', 'showCompass', 'showZoom', 'visualizePitch']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'position', 'showCompass', 'showZoom', 'visualizePitch']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(NavigationControl, self).__init__(**args)
