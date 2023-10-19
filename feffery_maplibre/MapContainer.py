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
    防抖监听参数，用于监听当前地图旋转角度.

- boundsDebounce (list; optional):
    防抖监听参数，用于监听当前地图坐标范围  格式为[经度下限, 纬度下限, 经度上限, 纬度上限].

- boxZoom (boolean; default False):
    用于设置是否开启框选放大功能，开启后用户可按住shift用鼠标在地图上绘制方框进行快速放大  默认：False.

- clickListenBoxSize (number; default 5):
    设置通过地图点击事件针对interactiveLayerIds所指定的图层进行监听时，以鼠标点击点为中心外扩box范围的像素边长
    默认：5.

- clickListenLayerCount (number; default 0):
    用于监听有效图层要素点击事件累积次数  默认：0.

- clickListenLayerFeatures (list; optional):
    用于监听最近一次地图点击事件对应clickListenLayerIds所查询到的相关图层要素信息.

- clickListenLayerIds (list; optional):
    设置通过地图交互事件允许监听的图层id数组  默认：[].

- clickedLngLat (dict; optional):
    用于监听最近一次地图点击事件对应的坐标信息及时间戳信息.

    `clickedLngLat` is a dict with keys:

    - lat (number; optional):
        点击位置纬度.

    - lng (number; optional):
        点击位置经度.

    - timestamp (number; optional):
        点击事件对应的时间戳.

- currentDrawMode (string; optional):
    用于监听当前地图绘制功能所对应的功能模式.

- cursor (string; optional):
    设置默认鼠标指针样式，同css中的cursor属性
    参考资料：https://developer.mozilla.org/en-US/docs/Web/CSS/cursor.

- debounceWait (number; default 200):
    设置针对当前地图容器的防抖延时，单位：毫秒  默认：200.

- debug (boolean; default False):
    开发调试专用，用于开启debug模式，开启后会在浏览器控制台打印主要事件信息  默认：False.

- doubleClickZoom (boolean; default True):
    用于设置是否允许双击放大地图  默认：True.

- dragPan (boolean; default True):
    设置是否允许鼠标拖拽平移地图  默认：True.

- dragRotate (boolean; default True):
    用于设置是否允许鼠标拖拽旋转地图  默认：True.

- drawCircleSteps (number; default 64):
    设置绘制圆形时，生成矢量中circle字段返回对应圆形矢量数据的精度，越大越精准  默认：64.

- drawControls (dict; optional):
    配置需要开启的功能控件种类.

    `drawControls` is a dict with keys:

    - combine_features (boolean; optional):
        用于设置是否为当前地图绘制控件开启已绘制要素组合功能  默认：False.

    - draw_circle (boolean; optional):
        特殊绘图模式，无自带的触发控件按钮，用于设置是否为当前地图绘制控件开启圆形绘制功能  默认：True.

    - line_string (boolean; optional):
        用于设置是否为当前地图绘制控件开启线绘制功能  默认：True.

    - point (boolean; optional):
        用于设置是否为当前地图绘制控件开启点绘制功能  默认：True.

    - polygon (boolean; optional):
        用于设置是否为当前地图绘制控件开启面绘制功能  默认：True.

    - trash (boolean; optional):
        用于设置是否为当前地图绘制控件开启已绘制要素删除功能  默认：True.

    - uncombine_features (boolean; optional):
        用于设置是否为当前地图绘制控件开启已绘制要素组合拆分功能  默认：False.

- drawControlsPosition (a value equal to: 'top-right', 'top-left', 'bottom-right', 'bottom-left'; default 'top-left'):
    设置地图绘制控件显示方位
    可选的有'top-right'、'top-left'、'bottom-right'、'bottom-left'
    默认：'top-left'.

- drawDeleteAll (boolean; default False):
    用于手动执行已绘制要素的清空操作，每次执行清空操作后会被重置为False  默认：False.

- drawDeleteSelected (boolean; default False):
    用于手动执行对已绘制要素中，处于选择状态下的要素进行删除，每次执行删除操作后会被重置为False  默认：False.

- drawOnlyOne (boolean; default False):
    设置是否在每次点击相应绘制功能按钮后清空先前的已绘制要素，从而确保同时最多存在一个已绘制要素  默认：False.

- drawSpatialJudgeListenLayerFeatures (list; optional):
    用于监听最近一次已绘制面要素对应drawSpatialJudgeListenLayerIds所查询到的相关图层要素信息.

- drawSpatialJudgeListenLayerIds (list; optional):
    设置通过要素绘制空间关系判断需要监听的目标图层id数组  默认：[].

- drawSpatialJudgePredicate (a value equal to: 'intersects', 'contains'; default 'intersects'):
    用于设置已绘制面要素与其他图层拓扑关联所依据的类型  可选的有'intersects'（相交）、'contains'（包含）
    默认：'intersects'.

- drawnFeatures (list; optional):
    用于监听通过绘图控件已绘制的要素数组.

- enableDraw (boolean; default False):
    用于设置是否为当前地图启用绘制控件功能  默认：False.

- enableDrawSpatialJudge (boolean; default False):
    当drawOnlyOne为True时生效，用于设置是否以绘制的面要素为范围，计算与之存在拓扑关联的其他图层要素  默认：False.

- initialViewState (dict; default {    longitude: 0,    latitude: 0,    zoom: 0,    pitch: 0,    bearing: 0,}):
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
    防抖监听参数，用于监听当前地图中心点纬度.

- loadedLayers (list; optional):
    用于监听最近一次图层加载事件后全部图层信息.

- loadedSources (dict; optional):
    用于监听最近一次图层加载事件后全部图层源信息.

- locale (a value equal to: 'zh-cn', 'en-us'; default 'zh-cn'):
    设置语言类型，可选的有'zh-cn'（简体中文）、'en-us'（英文）  默认：'zh-cn'.

- localeInfo (dict; optional):
    自定义常用文案信息  具体可设置文案键值对：  - NavigationControl.ZoomIn  -
    NavigationControl.ZoomOut  - NavigationControl.ResetBearing  -
    DrawControl.LineStringTool  - DrawControl.PolygonTool  -
    DrawControl.MarkerTool  - DrawControl.Delete  -
    DrawControl.Combine  - DrawControl.Uncombine
    其他参考资料：https://github.com/maplibre/maplibre-gl-js/blob/main/src/ui/default_locale.ts.

- longitude (number; optional):
    受控参数，用于设置或监听当前地图中心点经度.

- longitudeDebounce (number; optional):
    防抖监听参数，用于监听当前地图中心点经度.

- mapStyle (string | dict; optional):
    用于设置底图样式配置文件.

- mapboxAccessToken (string; optional):
    可选，用于配置mapbox服务token.

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
    防抖监听参数，用于监听当前地图倾斜角度.

- renderWorldCopies (boolean; default True):
    设置世界范围是否允许重复  默认：True.

- scrollZoom (boolean; default True):
    设置是否允许鼠标滚轮缩放地图  默认：True.

- setDrawMode (a value equal to: 'simple_select', 'draw_line_string', 'draw_polygon', 'draw_point', 'draw_circle'; optional):
    用于手动切换到指定地图绘制功能模式，每次成功切换模式后会重置为空.

- style (dict; optional):
    用于设置当前地图容器的css样式.

- terrain (dict; optional):
    用于配置terrain相关参数.

- touchPitch (boolean; default True):
    设置是否允许鼠标拖拽调整地图倾斜角度  默认：True.

- workerCount (number; default 2):
    设置开启的并行工作web worker数量  默认：2.

- zoom (number; optional):
    受控参数，用于设置或监听当前地图缩放级别.

- zoomDebounce (number; optional):
    防抖监听参数，用于监听当前地图缩放级别."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'MapContainer'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, cursor=Component.UNDEFINED, mapStyle=Component.UNDEFINED, renderWorldCopies=Component.UNDEFINED, initialViewState=Component.UNDEFINED, longitude=Component.UNDEFINED, latitude=Component.UNDEFINED, zoom=Component.UNDEFINED, pitch=Component.UNDEFINED, bearing=Component.UNDEFINED, minZoom=Component.UNDEFINED, maxZoom=Component.UNDEFINED, minPitch=Component.UNDEFINED, maxPitch=Component.UNDEFINED, maxBounds=Component.UNDEFINED, boxZoom=Component.UNDEFINED, doubleClickZoom=Component.UNDEFINED, dragRotate=Component.UNDEFINED, dragPan=Component.UNDEFINED, keyboard=Component.UNDEFINED, scrollZoom=Component.UNDEFINED, touchPitch=Component.UNDEFINED, clickListenLayerIds=Component.UNDEFINED, clickListenBoxSize=Component.UNDEFINED, enableDraw=Component.UNDEFINED, drawControls=Component.UNDEFINED, setDrawMode=Component.UNDEFINED, currentDrawMode=Component.UNDEFINED, drawControlsPosition=Component.UNDEFINED, drawOnlyOne=Component.UNDEFINED, drawCircleSteps=Component.UNDEFINED, drawnFeatures=Component.UNDEFINED, enableDrawSpatialJudge=Component.UNDEFINED, drawSpatialJudgePredicate=Component.UNDEFINED, drawSpatialJudgeListenLayerIds=Component.UNDEFINED, drawSpatialJudgeListenLayerFeatures=Component.UNDEFINED, drawDeleteAll=Component.UNDEFINED, drawDeleteSelected=Component.UNDEFINED, locale=Component.UNDEFINED, localeInfo=Component.UNDEFINED, interactive=Component.UNDEFINED, workerCount=Component.UNDEFINED, clickedLngLat=Component.UNDEFINED, clickListenLayerFeatures=Component.UNDEFINED, clickListenLayerCount=Component.UNDEFINED, loadedSources=Component.UNDEFINED, loadedLayers=Component.UNDEFINED, debounceWait=Component.UNDEFINED, longitudeDebounce=Component.UNDEFINED, latitudeDebounce=Component.UNDEFINED, zoomDebounce=Component.UNDEFINED, pitchDebounce=Component.UNDEFINED, bearingDebounce=Component.UNDEFINED, boundsDebounce=Component.UNDEFINED, debug=Component.UNDEFINED, mapboxAccessToken=Component.UNDEFINED, terrain=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bearing', 'bearingDebounce', 'boundsDebounce', 'boxZoom', 'clickListenBoxSize', 'clickListenLayerCount', 'clickListenLayerFeatures', 'clickListenLayerIds', 'clickedLngLat', 'currentDrawMode', 'cursor', 'debounceWait', 'debug', 'doubleClickZoom', 'dragPan', 'dragRotate', 'drawCircleSteps', 'drawControls', 'drawControlsPosition', 'drawDeleteAll', 'drawDeleteSelected', 'drawOnlyOne', 'drawSpatialJudgeListenLayerFeatures', 'drawSpatialJudgeListenLayerIds', 'drawSpatialJudgePredicate', 'drawnFeatures', 'enableDraw', 'enableDrawSpatialJudge', 'initialViewState', 'interactive', 'key', 'keyboard', 'latitude', 'latitudeDebounce', 'loadedLayers', 'loadedSources', 'locale', 'localeInfo', 'longitude', 'longitudeDebounce', 'mapStyle', 'mapboxAccessToken', 'maxBounds', 'maxPitch', 'maxZoom', 'minPitch', 'minZoom', 'pitch', 'pitchDebounce', 'renderWorldCopies', 'scrollZoom', 'setDrawMode', 'style', 'terrain', 'touchPitch', 'workerCount', 'zoom', 'zoomDebounce']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bearing', 'bearingDebounce', 'boundsDebounce', 'boxZoom', 'clickListenBoxSize', 'clickListenLayerCount', 'clickListenLayerFeatures', 'clickListenLayerIds', 'clickedLngLat', 'currentDrawMode', 'cursor', 'debounceWait', 'debug', 'doubleClickZoom', 'dragPan', 'dragRotate', 'drawCircleSteps', 'drawControls', 'drawControlsPosition', 'drawDeleteAll', 'drawDeleteSelected', 'drawOnlyOne', 'drawSpatialJudgeListenLayerFeatures', 'drawSpatialJudgeListenLayerIds', 'drawSpatialJudgePredicate', 'drawnFeatures', 'enableDraw', 'enableDrawSpatialJudge', 'initialViewState', 'interactive', 'key', 'keyboard', 'latitude', 'latitudeDebounce', 'loadedLayers', 'loadedSources', 'locale', 'localeInfo', 'longitude', 'longitudeDebounce', 'mapStyle', 'mapboxAccessToken', 'maxBounds', 'maxPitch', 'maxZoom', 'minPitch', 'minZoom', 'pitch', 'pitchDebounce', 'renderWorldCopies', 'scrollZoom', 'setDrawMode', 'style', 'terrain', 'touchPitch', 'workerCount', 'zoom', 'zoomDebounce']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MapContainer, self).__init__(children=children, **args)
