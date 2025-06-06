# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class MapContainer(Component):
    """A MapContainer component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- children (a list of or a singular dash component, string or number; optional):
    设置内部组件元素，从而实现更多地图定制化功能.

- key (string; optional):
    强制重绘当前组件时使用.

- cursor (string; optional):
    设置默认鼠标指针样式，同css中的cursor属性
    参考资料：https://developer.mozilla.org/en-US/docs/Web/CSS/cursor.

- mapStyle (string | dict; optional):
    用于设置底图样式配置文件.

- renderWorldCopies (boolean; default True):
    设置世界范围是否允许重复  默认：True.

- initialViewState (dict; optional):
    非受控参数，设置当前地图容器的初始视角相关参数
    参考资料：https://visgl.github.io/react-map-gl/docs/api-reference/map#initialviewstate.

    `initialViewState` is a dict with keys:

    - longitude (number; optional):
        用于设置初始视角对应地图中心点经度  默认：0.

    - latitude (number; optional):
        用于设置初始视角对应地图中心点纬度  默认：0.

    - zoom (number; optional):
        用于设置初始视角对应地图缩放级别  默认：0.

    - pitch (number; optional):
        用于设置初始视角对应地图倾斜角度  默认：0.

    - bearing (number; optional):
        用于设置初始视角对应地图旋转角度  默认：0.

    - bounds (list; optional):
        用于设置初始视角对应地图视角坐标范围  此项设置后会忽略已设置的longitude、latitude、zoom
        格式为[经度下限, 纬度下限, 经度上限, 纬度上限]  默认：None.

- longitude (number; optional):
    受控参数，用于设置或监听当前地图中心点经度.

- latitude (number; optional):
    受控参数，用于设置或监听当前地图中心点纬度.

- zoom (number; optional):
    受控参数，用于设置或监听当前地图缩放级别.

- pitch (number; optional):
    受控参数，用于设置或监听当前地图倾斜角度.

- bearing (number; optional):
    受控参数，用于设置或监听当前地图旋转角度.

- minZoom (number; default 0):
    用于设置当前地图最小缩放级别，取值应在0到24之间  默认：0.

- maxZoom (number; default 22):
    用于设置当前地图最大缩放级别，取值应在0到24之间  默认：22.

- minPitch (number; default 0):
    用于设置当前地图最小倾斜角度，取值应在0到85之间  默认：0.

- maxPitch (number; default 60):
    用于设置当前地图最大倾斜角度，取值应在0到85之间  默认：60.

- maxBounds (list; optional):
    用于限制当前地图视角坐标范围，用于限制用户可查看地图范围  格式为[经度下限, 纬度下限, 经度上限, 纬度上限]
    默认：None.

- boxZoom (boolean; default False):
    用于设置是否开启框选放大功能，开启后用户可按住shift用鼠标在地图上绘制方框进行快速放大  默认：False.

- doubleClickZoom (boolean; default True):
    用于设置是否允许双击放大地图  默认：True.

- dragRotate (boolean; default True):
    用于设置是否允许鼠标拖拽旋转地图  默认：True.

- dragPan (boolean; default True):
    设置是否允许鼠标拖拽平移地图  默认：True.

- keyboard (boolean; default True):
    设置是否允许通过键盘调整地图  默认：True.

- scrollZoom (boolean; default True):
    设置是否允许鼠标滚轮缩放地图  默认：True.

- touchPitch (boolean; default True):
    设置是否允许鼠标拖拽调整地图倾斜角度  默认：True.

- clickListenLayerIds (list; optional):
    设置通过地图交互事件允许监听的图层id数组  默认：[].

- clickListenBoxSize (number; default 5):
    设置通过地图点击事件针对interactiveLayerIds所指定的图层进行监听时，以鼠标点击点为中心外扩box范围的像素边长
    默认：5.

- enableDraw (boolean; default False):
    用于设置是否为当前地图启用绘制控件功能  默认：False.

- drawControls (dict; optional):
    配置需要显示内置操作按钮的功能控件种类.

    `drawControls` is a dict with keys:

    - point (boolean; optional):
        用于设置是否为当前地图绘制控件开启点绘制功能  默认：True.

    - line_string (boolean; optional):
        用于设置是否为当前地图绘制控件开启线绘制功能  默认：True.

    - polygon (boolean; optional):
        用于设置是否为当前地图绘制控件开启面绘制功能  默认：True.

    - trash (boolean; optional):
        用于设置是否为当前地图绘制控件开启已绘制要素删除功能  默认：True.

    - combine_features (boolean; optional):
        用于设置是否为当前地图绘制控件开启已绘制要素组合功能  默认：False.

    - uncombine_features (boolean; optional):
        用于设置是否为当前地图绘制控件开启已绘制要素组合拆分功能  默认：False.

- setDrawMode (a value equal to: 'simple_select', 'draw_line_string', 'draw_polygon', 'draw_point', 'draw_circle', 'freehand_polygon'; optional):
    用于手动切换到指定地图绘制功能模式，每次成功切换模式后会重置为空.

- currentDrawMode (string; optional):
    用于监听当前地图绘制功能所对应的功能模式.

- drawControlsPosition (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'top-left'):
    设置地图绘制控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'top-left'.

- drawOnlyOne (boolean; default False):
    设置是否在每次点击相应绘制功能按钮后清空先前的已绘制要素，从而确保同时最多存在一个已绘制要素  默认：False.

- drawCircleSteps (number; default 64):
    设置绘制圆形时，生成矢量中circle字段返回对应圆形矢量数据的精度，越大越精准  默认：64.

- drawStyles (list; optional):
    添加矢量绘制自定义样式规则，具体参考：https://github.com/mapbox/mapbox-gl-draw/blob/main/docs/API.md#styling-draw.

- drawnFeatures (list; optional):
    用于监听通过绘图控件已绘制的要素数组.

- enableDrawSpatialJudge (boolean; default False):
    当drawOnlyOne为True时生效，用于设置是否以绘制的面要素为范围，计算与之存在拓扑关联的其他图层要素  默认：False.

- drawSpatialJudgePredicate (a value equal to: 'intersects', 'contains'; default 'intersects'):
    用于设置已绘制面要素与其他图层拓扑关联所依据的类型  可选的有'intersects'（相交）、'contains'（包含）
    默认：'intersects'.

- drawSpatialJudgeListenLayerIds (list; optional):
    设置通过要素绘制空间关系判断需要监听的目标图层id数组  默认：[].

- drawSpatialJudgeListenLayerFeatures (list; optional):
    用于监听最近一次已绘制面要素对应drawSpatialJudgeListenLayerIds所查询到的相关图层要素信息.

- drawDeleteAll (boolean; default False):
    用于手动执行已绘制要素的清空操作，每次执行清空操作后会被重置为False  默认：False.

- drawDeleteSelected (boolean; default False):
    用于手动执行对已绘制要素中，处于选择状态下的要素进行删除，每次执行删除操作后会被重置为False  默认：False.

- locale (a value equal to: 'zh-cn', 'en-us'; default 'zh-cn'):
    设置语言类型，可选的有'zh-cn'（简体中文）、'en-us'（英文）  默认：'zh-cn'.

- localeInfo (dict; optional):
    自定义常用文案信息  具体可设置文案键值对：  - NavigationControl.ZoomIn  -
    NavigationControl.ZoomOut  - NavigationControl.ResetBearing  -
    DrawControl.LineStringTool  - DrawControl.PolygonTool  -
    DrawControl.MarkerTool  - DrawControl.Delete  -
    DrawControl.Combine  - DrawControl.Uncombine
    其他参考资料：https://github.com/maplibre/maplibre-gl-js/blob/main/src/ui/default_locale.ts.

- interactive (boolean; default True):
    设置是否开启地图交互事件监听功能  默认：True.

- workerCount (number; default 2):
    设置开启的并行工作web worker数量  默认：2.

- resizeEventCount (number; default 0):
    监听resize事件累积触发次数  默认：0.

- wheelEventCount (number; default 0):
    监听wheel事件累积触发次数  默认：0.

- moveStartEventCount (number; default 0):
    监听movestart事件累积触发次数  默认：0.

- dragStartEventCount (number; default 0):
    监听dragStart事件累积触发次数  默认：0.

- clickedLngLat (dict; optional):
    用于监听最近一次地图点击事件对应的坐标信息及时间戳信息.

    `clickedLngLat` is a dict with keys:

    - lng (number; optional):
        点击位置经度.

    - lat (number; optional):
        点击位置纬度.

    - timestamp (number; optional):
        点击事件对应的时间戳.

- hoveredLngLat (dict; optional):
    用于监听最近一次地图鼠标悬停事件对应的坐标信息及时间戳信息.

    `hoveredLngLat` is a dict with keys:

    - lng (number; optional):
        点击位置经度.

    - lat (number; optional):
        点击位置纬度.

    - timestamp (number; optional):
        点击事件对应的时间戳.

- clickListenLayerFeatures (list; optional):
    用于监听最近一次地图点击事件对应clickListenLayerIds所查询到的相关图层要素信息.

- clickListenLayerCount (number; default 0):
    用于监听有效图层要素点击事件累积次数  默认：0.

- loadedSources (dict; optional):
    用于监听最近一次图层加载事件后全部图层源信息.

- loadedLayers (list; optional):
    用于监听最近一次图层加载事件后全部图层信息.

- debounceWait (number; default 200):
    设置针对当前地图容器的防抖延时，单位：毫秒  默认：200.

- longitudeDebounce (number; optional):
    防抖监听参数，用于监听当前地图中心点经度.

- latitudeDebounce (number; optional):
    防抖监听参数，用于监听当前地图中心点纬度.

- zoomDebounce (number; optional):
    防抖监听参数，用于监听当前地图缩放级别.

- pitchDebounce (number; optional):
    防抖监听参数，用于监听当前地图倾斜角度.

- bearingDebounce (number; optional):
    防抖监听参数，用于监听当前地图旋转角度.

- boundsDebounce (list; optional):
    防抖监听参数，用于监听当前地图坐标范围  格式为[经度下限, 纬度下限, 经度上限, 纬度上限].

- debug (boolean; default False):
    开发调试专用，用于开启debug模式，开启后会在浏览器控制台打印主要事件信息  默认：False.

- debugProps (list of a value equal to: 'viewState', 'loadedSources', 'loadedLayers', 'clickedLngLat', 'hoveredLngLat's; default ['viewState', 'loadedSources', 'loadedLayers', 'clickedLngLat', 'hoveredLngLat']):
    开发调试专用，用于在debug=True时，设置具体需要展示的属性名  默认：['viewState',
    'loadedSources', 'loadedLayers', 'clickedLngLat',
    'hoveredLngLat'].

- mapboxAccessToken (string; optional):
    可选，用于配置mapbox服务token.

- terrain (dict; optional):
    用于配置terrain相关参数."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'MapContainer'
    InitialViewState = TypedDict(
        "InitialViewState",
            {
            "longitude": NotRequired[NumberType],
            "latitude": NotRequired[NumberType],
            "zoom": NotRequired[NumberType],
            "pitch": NotRequired[NumberType],
            "bearing": NotRequired[NumberType],
            "bounds": NotRequired[typing.Sequence]
        }
    )

    DrawControls = TypedDict(
        "DrawControls",
            {
            "point": NotRequired[bool],
            "line_string": NotRequired[bool],
            "polygon": NotRequired[bool],
            "trash": NotRequired[bool],
            "combine_features": NotRequired[bool],
            "uncombine_features": NotRequired[bool]
        }
    )

    ClickedLngLat = TypedDict(
        "ClickedLngLat",
            {
            "lng": NotRequired[NumberType],
            "lat": NotRequired[NumberType],
            "timestamp": NotRequired[NumberType]
        }
    )

    HoveredLngLat = TypedDict(
        "HoveredLngLat",
            {
            "lng": NotRequired[NumberType],
            "lat": NotRequired[NumberType],
            "timestamp": NotRequired[NumberType]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        cursor: typing.Optional[str] = None,
        mapStyle: typing.Optional[typing.Union[str, dict]] = None,
        renderWorldCopies: typing.Optional[bool] = None,
        initialViewState: typing.Optional["InitialViewState"] = None,
        longitude: typing.Optional[NumberType] = None,
        latitude: typing.Optional[NumberType] = None,
        zoom: typing.Optional[NumberType] = None,
        pitch: typing.Optional[NumberType] = None,
        bearing: typing.Optional[NumberType] = None,
        minZoom: typing.Optional[NumberType] = None,
        maxZoom: typing.Optional[NumberType] = None,
        minPitch: typing.Optional[NumberType] = None,
        maxPitch: typing.Optional[NumberType] = None,
        maxBounds: typing.Optional[typing.Sequence] = None,
        boxZoom: typing.Optional[bool] = None,
        doubleClickZoom: typing.Optional[bool] = None,
        dragRotate: typing.Optional[bool] = None,
        dragPan: typing.Optional[bool] = None,
        keyboard: typing.Optional[bool] = None,
        scrollZoom: typing.Optional[bool] = None,
        touchPitch: typing.Optional[bool] = None,
        clickListenLayerIds: typing.Optional[typing.Sequence] = None,
        clickListenBoxSize: typing.Optional[NumberType] = None,
        enableDraw: typing.Optional[bool] = None,
        drawControls: typing.Optional["DrawControls"] = None,
        setDrawMode: typing.Optional[Literal["simple_select", "draw_line_string", "draw_polygon", "draw_point", "draw_circle", "freehand_polygon"]] = None,
        currentDrawMode: typing.Optional[str] = None,
        drawControlsPosition: typing.Optional[Literal["top-right", "top-left", "bottom-right", "bottom-left"]] = None,
        drawOnlyOne: typing.Optional[bool] = None,
        drawCircleSteps: typing.Optional[NumberType] = None,
        drawStyles: typing.Optional[typing.Sequence] = None,
        drawnFeatures: typing.Optional[typing.Sequence] = None,
        enableDrawSpatialJudge: typing.Optional[bool] = None,
        drawSpatialJudgePredicate: typing.Optional[Literal["intersects", "contains"]] = None,
        drawSpatialJudgeListenLayerIds: typing.Optional[typing.Sequence] = None,
        drawSpatialJudgeListenLayerFeatures: typing.Optional[typing.Sequence] = None,
        drawDeleteAll: typing.Optional[bool] = None,
        drawDeleteSelected: typing.Optional[bool] = None,
        locale: typing.Optional[Literal["zh-cn", "en-us"]] = None,
        localeInfo: typing.Optional[dict] = None,
        interactive: typing.Optional[bool] = None,
        workerCount: typing.Optional[NumberType] = None,
        resizeEventCount: typing.Optional[NumberType] = None,
        wheelEventCount: typing.Optional[NumberType] = None,
        moveStartEventCount: typing.Optional[NumberType] = None,
        dragStartEventCount: typing.Optional[NumberType] = None,
        clickedLngLat: typing.Optional["ClickedLngLat"] = None,
        hoveredLngLat: typing.Optional["HoveredLngLat"] = None,
        clickListenLayerFeatures: typing.Optional[typing.Sequence] = None,
        clickListenLayerCount: typing.Optional[NumberType] = None,
        loadedSources: typing.Optional[dict] = None,
        loadedLayers: typing.Optional[typing.Sequence] = None,
        debounceWait: typing.Optional[NumberType] = None,
        longitudeDebounce: typing.Optional[NumberType] = None,
        latitudeDebounce: typing.Optional[NumberType] = None,
        zoomDebounce: typing.Optional[NumberType] = None,
        pitchDebounce: typing.Optional[NumberType] = None,
        bearingDebounce: typing.Optional[NumberType] = None,
        boundsDebounce: typing.Optional[typing.Sequence] = None,
        debug: typing.Optional[bool] = None,
        debugProps: typing.Optional[typing.Sequence[Literal["viewState", "loadedSources", "loadedLayers", "clickedLngLat", "hoveredLngLat"]]] = None,
        mapboxAccessToken: typing.Optional[str] = None,
        terrain: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'children', 'key', 'style', 'cursor', 'mapStyle', 'renderWorldCopies', 'initialViewState', 'longitude', 'latitude', 'zoom', 'pitch', 'bearing', 'minZoom', 'maxZoom', 'minPitch', 'maxPitch', 'maxBounds', 'boxZoom', 'doubleClickZoom', 'dragRotate', 'dragPan', 'keyboard', 'scrollZoom', 'touchPitch', 'clickListenLayerIds', 'clickListenBoxSize', 'enableDraw', 'drawControls', 'setDrawMode', 'currentDrawMode', 'drawControlsPosition', 'drawOnlyOne', 'drawCircleSteps', 'drawStyles', 'drawnFeatures', 'enableDrawSpatialJudge', 'drawSpatialJudgePredicate', 'drawSpatialJudgeListenLayerIds', 'drawSpatialJudgeListenLayerFeatures', 'drawDeleteAll', 'drawDeleteSelected', 'locale', 'localeInfo', 'interactive', 'workerCount', 'resizeEventCount', 'wheelEventCount', 'moveStartEventCount', 'dragStartEventCount', 'clickedLngLat', 'hoveredLngLat', 'clickListenLayerFeatures', 'clickListenLayerCount', 'loadedSources', 'loadedLayers', 'debounceWait', 'longitudeDebounce', 'latitudeDebounce', 'zoomDebounce', 'pitchDebounce', 'bearingDebounce', 'boundsDebounce', 'debug', 'debugProps', 'mapboxAccessToken', 'terrain']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'key', 'style', 'cursor', 'mapStyle', 'renderWorldCopies', 'initialViewState', 'longitude', 'latitude', 'zoom', 'pitch', 'bearing', 'minZoom', 'maxZoom', 'minPitch', 'maxPitch', 'maxBounds', 'boxZoom', 'doubleClickZoom', 'dragRotate', 'dragPan', 'keyboard', 'scrollZoom', 'touchPitch', 'clickListenLayerIds', 'clickListenBoxSize', 'enableDraw', 'drawControls', 'setDrawMode', 'currentDrawMode', 'drawControlsPosition', 'drawOnlyOne', 'drawCircleSteps', 'drawStyles', 'drawnFeatures', 'enableDrawSpatialJudge', 'drawSpatialJudgePredicate', 'drawSpatialJudgeListenLayerIds', 'drawSpatialJudgeListenLayerFeatures', 'drawDeleteAll', 'drawDeleteSelected', 'locale', 'localeInfo', 'interactive', 'workerCount', 'resizeEventCount', 'wheelEventCount', 'moveStartEventCount', 'dragStartEventCount', 'clickedLngLat', 'hoveredLngLat', 'clickListenLayerFeatures', 'clickListenLayerCount', 'loadedSources', 'loadedLayers', 'debounceWait', 'longitudeDebounce', 'latitudeDebounce', 'zoomDebounce', 'pitchDebounce', 'bearingDebounce', 'boundsDebounce', 'debug', 'debugProps', 'mapboxAccessToken', 'terrain']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MapContainer, self).__init__(children=children, **args)

setattr(MapContainer, "__init__", _explicitize_args(MapContainer.__init__))
