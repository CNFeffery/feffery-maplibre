# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Resize(Component):
    """A Resize component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- delay (number; optional):
    设置动作延时，单位：毫秒.

- key (string; optional):
    强制重绘当前组件时使用.

- resize (boolean; default False):
    设置为True时用于触发地图resize事件，每次执行完成后会自动重置为False  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Resize'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, resize=Component.UNDEFINED, delay=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'delay', 'key', 'resize']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'delay', 'key', 'resize']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Resize, self).__init__(**args)
