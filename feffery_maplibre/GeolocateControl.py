# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GeolocateControl(Component):
    """A GeolocateControl component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- geolocateInfo (dict; optional):
    监听最近一次定位相关信息.

- key (string; optional):
    强制重绘当前组件时使用.

- position (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'bottom-right'):
    设置当前定位控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'bottom-right'.

- positionOptions (dict; optional):
    配置定位相关行为参数.

    `positionOptions` is a dict with keys:

    - enableHighAccuracy (boolean; optional):
        是否开启高精度定位  默认：False.

    - maximumAge (number; optional):
        定位信息缓存时长，单位：毫秒  默认：0，即不缓存.

    - timeout (number; optional):
        定位请求超时时长，单位：毫秒  默认：6000.

- showAccuracyCircle (boolean; default True):
    是否展示定位范围95%置信区间圆圈，当showUserLocation为False时会自动禁用  默认：True.

- showUserHeading (boolean; default False):
    是否展示定位点方向标记，仅在trackUserLocation为True时可用  默认：False.

- showUserLocation (boolean; default True):
    是否展示定位点标记  默认：True.

- style (dict; optional):
    用于设置当前控件容器的css样式.

- trackUserLocation (boolean; default False):
    是否持续监听用户位置  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'GeolocateControl'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, position=Component.UNDEFINED, positionOptions=Component.UNDEFINED, showUserLocation=Component.UNDEFINED, showAccuracyCircle=Component.UNDEFINED, showUserHeading=Component.UNDEFINED, trackUserLocation=Component.UNDEFINED, geolocateInfo=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'geolocateInfo', 'key', 'position', 'positionOptions', 'showAccuracyCircle', 'showUserHeading', 'showUserLocation', 'style', 'trackUserLocation']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'geolocateInfo', 'key', 'position', 'positionOptions', 'showAccuracyCircle', 'showUserHeading', 'showUserLocation', 'style', 'trackUserLocation']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(GeolocateControl, self).__init__(**args)
