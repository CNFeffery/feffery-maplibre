# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SortLayers(Component):
    """A SortLayers component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- key (string; optional):
    强制重绘当前组件时使用.

- orders (list of strings; optional):
    设置要针对当前地图实例中的相关图层进行重排序的顺序图层id数组，越靠后的元素在此次排序之后图层顺序越高
    每次新的执行完成后会自动重置为[]  默认：None."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'SortLayers'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, orders=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'orders']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'orders']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(SortLayers, self).__init__(**args)
