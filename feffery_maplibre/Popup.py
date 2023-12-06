# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Popup(Component):
    """A Popup component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    设置内部元素，用于代替缺省的标记图标.

- id (string; optional):
    必填，用于唯一标识当前组件.

- anchor (a value equal to: 'center', 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right'; optional):
    当前弹出卡片相对坐标点的方位
    可选的有'center'、'top'、'bottom'、'left'、'right'、'top-left'、'top-right'、'bottom-left'、'bottom-right'
    默认：'center'.

- className (string; optional):
    用于设置当前弹出卡片的css类名.

- closeButton (boolean; default True):
    是否显示关闭按钮  默认：True.

- closeOnClick (boolean; default True):
    点击地图其他位置是否触发关闭  默认：True.

- closeOnMove (boolean; default False):
    地图移动时是否触发关闭  默认：False.

- key (string; optional):
    强制重绘当前组件时使用.

- latitude (number; required):
    必填，设置当前标记对应位置纬度.

- longitude (number; required):
    必填，设置当前标记对应位置经度.

- maxWidth (string; default '240px'):
    设置当前弹出卡片的最大宽度  默认：'240px'.

- offset (list of numbers; optional):
    设置当前弹出卡片在水平和竖直方向上需要进行的像素偏移  格式如：[水平像素偏移, 竖直像素偏移].

- style (dict; optional):
    用于设置当前弹出卡片的css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'Popup'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, latitude=Component.REQUIRED, longitude=Component.REQUIRED, anchor=Component.UNDEFINED, maxWidth=Component.UNDEFINED, closeButton=Component.UNDEFINED, closeOnMove=Component.UNDEFINED, closeOnClick=Component.UNDEFINED, offset=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'anchor', 'className', 'closeButton', 'closeOnClick', 'closeOnMove', 'key', 'latitude', 'longitude', 'maxWidth', 'offset', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'anchor', 'className', 'closeButton', 'closeOnClick', 'closeOnMove', 'key', 'latitude', 'longitude', 'maxWidth', 'offset', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['latitude', 'longitude']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Popup, self).__init__(children=children, **args)
