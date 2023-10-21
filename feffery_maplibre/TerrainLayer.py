# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TerrainLayer(Component):
    """A TerrainLayer component.


Keyword arguments:

- id (string; optional):
    用于唯一标识当前图层.

- bounds (list of numbers; optional):
    设置当前地形图层作用范围  格式为：[min_x, min_y, max_x, max_y].

- color (list of numbers; default [255, 255, 255]):
    当参数texture为空时，用于手动设置地形渲染颜色  默认：[255, 255, 255].

- elevationData (string; required):
    必填，设置高程地图服务地址.

- elevationDecoder (dict; default {    rScaler: 6553.6,    gScaler: 25.6,    bScaler: 0.1,    offset: -10000}):
    自定义rgb高程数据解码规则，默认为mapbox-rgb规则.

    `elevationDecoder` is a dict with keys:

    - bScaler (number; optional):
        蓝色通道系数.

    - gScaler (number; optional):
        绿色通道系数.

    - offset (number; optional):
        偏移系数.

    - rScaler (number; optional):
        红色通道系数.

- key (string; optional):
    强制重绘当前组件时使用.

- material (boolean; default True):
    设置是否开启材质效果  默认：True.

- texture (string; optional):
    设置随高程被拉伸的瓦片地图服务地址.

- wireframe (boolean; default False):
    设置是否渲染地形骨架线框  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'TerrainLayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, elevationData=Component.REQUIRED, texture=Component.UNDEFINED, elevationDecoder=Component.UNDEFINED, bounds=Component.UNDEFINED, color=Component.UNDEFINED, wireframe=Component.UNDEFINED, material=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bounds', 'color', 'elevationData', 'elevationDecoder', 'key', 'material', 'texture', 'wireframe']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bounds', 'color', 'elevationData', 'elevationDecoder', 'key', 'material', 'texture', 'wireframe']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['elevationData']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(TerrainLayer, self).__init__(**args)
