# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AddImages(Component):
    """An AddImages component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- key (string; optional):
    强制重绘当前组件时使用.

- images (list of dicts; optional):
    设置最新一次需要向当前地图实例添加的静态图片资源信息  默认：[].

    `images` is a list of dicts with keys:

    - id (string; required):
        当前图片资源id.

    - url (string; required):
        当前图片资源地址."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'AddImages'
    Images = TypedDict(
        "Images",
            {
            "id": str,
            "url": str
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        images: typing.Optional[typing.Sequence["Images"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'images']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'images']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AddImages, self).__init__(**args)
