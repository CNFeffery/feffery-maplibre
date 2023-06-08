# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class HandleRawMap(Component):
    """A HandleRawMap component.


Keyword arguments:

- id (string; required):
    必填，用于唯一标识当前图层.

- jsString (string; optional):
    设置要针对当前地图实例中的map对象执行的javascript代码字符串  每次新的执行完成后会自动重置为None
    默认：None.

- key (string; optional):
    强制重绘当前组件时使用."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'HandleRawMap'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, key=Component.UNDEFINED, jsString=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'jsString', 'key']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'jsString', 'key']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(HandleRawMap, self).__init__(**args)
