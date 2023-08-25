# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AddImages(Component):
    """An AddImages component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- images (list of dicts; optional):
    设置最新一次需要向当前地图实例添加的静态图片资源信息  默认：[].

    `images` is a list of dicts with keys:

    - id (string; required):
        当前图片资源id.

    - url (string; required):
        当前图片资源地址.

- key (string; optional):
    强制重绘当前组件时使用."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'AddImages'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, images=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'images', 'key']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'images', 'key']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AddImages, self).__init__(**args)
