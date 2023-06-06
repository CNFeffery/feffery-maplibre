# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MapContainer(Component):
    """A MapContainer component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    设置内部组件元素，从而实现更多地图定制化功能.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- bearing (number; optional):
    受控参数，用于设置或监听当前地图旋转角度.

- bearingDebounce (number; optional):
    防抖监听参数，用于设置或监听当前地图旋转角度.

- clickedLngLat (dict; optional):
    用于监听最近一次地图点击事件对应的坐标信息及时间戳信息.

    `clickedLngLat` is a dict with keys:

    - lat (number; optional):
        点击位置纬度.

    - lng (number; optional):
        点击位置经度.

    - timestamp (number; optional):
        点击事件对应的时间戳.

- cursor (string; optional):
    设置默认鼠标指针样式，同css中的cursor属性
    参考资料：https://developer.mozilla.org/en-US/docs/Web/CSS/cursor.

- debounceWait (number; default 200):
    设置针对当前地图容器的防抖延时，单位：毫秒  默认：200.

- doubleClickZoom (boolean; default True):
    用于设置是否允许双击放大地图  默认：True.

- dragPan (boolean; default True):
    设置是否允许鼠标拖拽平移地图  默认：True.

- dragRotate (boolean; default True):
    用于设置是否允许鼠标拖拽旋转地图  默认：True.

- enableDraw (boolean; default False):
    用于设置是否为当前地图启用绘制控件功能  默认：False.

- initialViewState (dict; optional):
    非受控参数，设置当前地图容器的初始视角相关参数
    参考资料：https://visgl.github.io/react-map-gl/docs/api-reference/map#initialviewstate.

    `initialViewState` is a dict with keys:

    - bearing (number; optional):
        用于设置初始视角对应地图旋转角度  默认：0.

    - bounds (list; optional):
        用于设置初始视角对应地图视角坐标范围  此项设置后会忽略已设置的longitude、latitude、zoom
        格式为[经度下限, 纬度下限, 经度上限, 纬度上限]  默认：None.

    - latitude (number; optional):
        用于设置初始视角对应地图中心点纬度  默认：0.

    - longitude (number; optional):
        用于设置初始视角对应地图中心点经度  默认：0.

    - pitch (number; optional):
        用于设置初始视角对应地图倾斜角度  默认：0.

    - zoom (number; optional):
        用于设置初始视角对应地图缩放级别  默认：0.

- interactive (boolean; default True):
    设置是否开启地图交互事件监听功能  默认：True.

- key (string; optional):
    强制重绘当前组件时使用.

- keyboard (boolean; default True):
    设置是否允许通过键盘调整地图  默认：True.

- latitude (number; optional):
    受控参数，用于设置或监听当前地图中心点纬度.

- latitudeDebounce (number; optional):
    防抖监听参数，用于设置或监听当前地图中心点纬度.

- locale (dict; optional):
    自定义常用文案信息
    参考资料：https://github.com/maplibre/maplibre-gl-js/blob/main/src/ui/default_locale.ts.

- longitude (number; optional):
    受控参数，用于设置或监听当前地图中心点经度.

- longitudeDebounce (number; optional):
    防抖监听参数，用于监听当前地图中心点经度.

- mapStyle (string | dict; optional):
    用于设置底图样式配置文件.

- mapboxAccessToken (string; optional):
    用于设置mapbox服务对应token.

- maxBounds (list; optional):
    用于限制当前地图视角坐标范围，用于限制用户可查看地图范围  格式为[经度下限, 纬度下限, 经度上限, 纬度上限]
    默认：None.

- maxPitch (number; default 60):
    用于设置当前地图最大倾斜角度，取值应在0到85之间  默认：60.

- maxZoom (number; default 22):
    用于设置当前地图最大缩放级别，取值应在0到24之间  默认：22.

- minPitch (number; default 0):
    用于设置当前地图最小倾斜角度，取值应在0到85之间  默认：0.

- minZoom (number; default 0):
    用于设置当前地图最小缩放级别，取值应在0到24之间  默认：0.

- pitch (number; optional):
    受控参数，用于设置或监听当前地图倾斜角度.

- pitchDebounce (number; optional):
    防抖监听参数，用于设置或监听当前地图倾斜角度.

- renderWorldCopies (boolean; default True):
    设置世界范围是否允许重复  默认：True.

- scrollZoom (boolean; default True):
    设置是否允许鼠标滚轮缩放地图  默认：True.

- style (dict; optional):
    用于设置当前地图容器的css样式.

- touchPitch (boolean; default True):
    设置是否允许鼠标拖拽调整地图倾斜角度  默认：True.

- workerCount (number; default 2):
    设置开启的并行工作web worker数量  默认：2.

- zoom (number; optional):
    受控参数，用于设置或监听当前地图缩放级别.

- zoomDebounce (number; optional):
    防抖监听参数，用于设置或监听当前地图缩放级别."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'MapContainer'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, cursor=Component.UNDEFINED, mapStyle=Component.UNDEFINED, renderWorldCopies=Component.UNDEFINED, initialViewState=Component.UNDEFINED, longitude=Component.UNDEFINED, latitude=Component.UNDEFINED, zoom=Component.UNDEFINED, pitch=Component.UNDEFINED, bearing=Component.UNDEFINED, minZoom=Component.UNDEFINED, maxZoom=Component.UNDEFINED, minPitch=Component.UNDEFINED, maxPitch=Component.UNDEFINED, maxBounds=Component.UNDEFINED, doubleClickZoom=Component.UNDEFINED, dragRotate=Component.UNDEFINED, dragPan=Component.UNDEFINED, keyboard=Component.UNDEFINED, scrollZoom=Component.UNDEFINED, touchPitch=Component.UNDEFINED, enableDraw=Component.UNDEFINED, mapboxAccessToken=Component.UNDEFINED, locale=Component.UNDEFINED, interactive=Component.UNDEFINED, workerCount=Component.UNDEFINED, clickedLngLat=Component.UNDEFINED, debounceWait=Component.UNDEFINED, longitudeDebounce=Component.UNDEFINED, latitudeDebounce=Component.UNDEFINED, zoomDebounce=Component.UNDEFINED, pitchDebounce=Component.UNDEFINED, bearingDebounce=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bearing', 'bearingDebounce', 'clickedLngLat', 'cursor', 'debounceWait', 'doubleClickZoom', 'dragPan', 'dragRotate', 'enableDraw', 'initialViewState', 'interactive', 'key', 'keyboard', 'latitude', 'latitudeDebounce', 'locale', 'longitude', 'longitudeDebounce', 'mapStyle', 'mapboxAccessToken', 'maxBounds', 'maxPitch', 'maxZoom', 'minPitch', 'minZoom', 'pitch', 'pitchDebounce', 'renderWorldCopies', 'scrollZoom', 'style', 'touchPitch', 'workerCount', 'zoom', 'zoomDebounce']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bearing', 'bearingDebounce', 'clickedLngLat', 'cursor', 'debounceWait', 'doubleClickZoom', 'dragPan', 'dragRotate', 'enableDraw', 'initialViewState', 'interactive', 'key', 'keyboard', 'latitude', 'latitudeDebounce', 'locale', 'longitude', 'longitudeDebounce', 'mapStyle', 'mapboxAccessToken', 'maxBounds', 'maxPitch', 'maxZoom', 'minPitch', 'minZoom', 'pitch', 'pitchDebounce', 'renderWorldCopies', 'scrollZoom', 'style', 'touchPitch', 'workerCount', 'zoom', 'zoomDebounce']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MapContainer, self).__init__(children=children, **args)
