# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GeoJsonLayer(Component):
    """A GeoJsonLayer component.


Keyword arguments:

- id (string; optional):
    用于唯一标识当前图层.

- autoHighlight (boolean; default False):
    当pickable为True时有效，用于设置是否自动高亮鼠标悬停的要素  默认：False.

- clickEvent (dict; optional):
    监听鼠标点击事件相关参数.

- data (list | string; optional):
    为当前图层设置数据源，当传入字符串时，代表数据源对应的url地址  默认：[].

- debounceWait (number; default 200):
    设置事件监听防抖延时，单位：毫秒  默认：200.

- elevationScale (number; default 1):
    extruded为True时有效，设置高度拉伸系数  默认：1.

- extruded (boolean; default False):
    针对多边形，设置是否进行高度拉伸，配合getElevation参数使用  默认：False.

- filled (boolean; default True):
    设置是否针对要素中的多边形及渲染为圆圈的点要素进行填充绘制  默认：True.

- getElevation (dict; default 1000):
    extruded=True时，针对拉伸高度的多边形，控制高度驱动方式  默认：1000.

    `getElevation` is a number | string | dict with keys:

    - func (string; optional)

- getFillColor (list of dicts; default [0, 0, 0, 255]):
    filled=True时，针对要素中的多边形及渲染为圆圈的点要素，控制填充颜色驱动方式  默认：[0, 0, 0, 255].

    `getFillColor` is a list | string | dict with keys:

    - func (string; optional)

- getLineColor (list of dicts; default [0, 0, 0, 255]):
    针对线要素及其他要素轮廓线，控制线条颜色驱动方式.

    `getLineColor` is a list | string | dict with keys:

    - func (string; optional)

- getLineWidth (dict; default 1):
    针对线要素及其他要素轮廓线，控制线条宽度驱动方式  默认：1.

    `getLineWidth` is a number | string | dict with keys:

    - func (string; optional)

- getPointRadius (dict; default 1):
    针对以圆圈形式渲染的点要素，控制圆圈半径驱动方式  默认：1.

    `getPointRadius` is a number | string | dict with keys:

    - func (string; optional)

- highlightColor (list; default [0, 0, 128, 128]):
    设置鼠标悬停要素高亮色  接受格式如[r, g, b, a]或[r, g, b]  默认：[0, 0, 128, 128].

- hoverEvent (dict; optional):
    监听鼠标悬停事件相关参数.

- key (string; optional):
    强制重绘当前组件时使用.

- lineBillboard (boolean; default False):
    针对线要素及其他要素的轮廓线，设置线条是否随着视角变化，而始终面朝屏幕视角  默认：False.

- lineWidthMaxPixels (number; optional):
    针对线要素及其他要素的轮廓线，设置线条最大显示宽度，单位：像素  默认无限制.

- lineWidthMinPixels (number; default 1):
    针对线要素及其他要素的轮廓线，设置线条最小显示宽度，单位：像素  默认：1.

- lineWidthScale (number; default 1):
    针对线要素及其他要素的轮廓线，设置宽度扩张系数  默认：1.

- lineWidthUnits (a value equal to: 'meters', 'common', 'pixels'; default 'pixels'):
    针对线要素及其他要素的轮廓线，设置宽度值对应的单位  可选的有'meters'、'common'、'pixels'
    默认：'pixels'
    参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units.

- opacity (number; default 1):
    设置当前图层透明度  默认：1.

- pickable (boolean; default False):
    设置是否启用鼠标交互事件  默认：False.

- pointBillboard (boolean; default False):
    pointType='circle'时有效，设置圆圈是否随着视角变化，而始终面朝屏幕视角  默认：False.

- pointRadiusMaxPixels (number; optional):
    pointType='circle'时有效，设置圆圈最大显示半径，单位：像素  默认无限制.

- pointRadiusMinPixels (number; default 0):
    pointType='circle'时有效，设置圆圈最小显示半径，单位：像素  默认：1.

- pointRadiusScale (number; default 1):
    pointType='circle'时有效，设置圆圈半径扩张系数  默认：1.

- pointRadiusUnits (a value equal to: 'meters', 'common', 'pixels'; default 'meters'):
    pointType='circle'时有效，设置圆圈半径对应的单位  可选的有'meters'、'common'、'pixels'
    默认：'pixels'
    参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units.

- pointType (a value equal to: 'circle', 'icon', 'text'; default 'circle'):
    设置针对点要素进行渲染的类型，可选的有'circle'、'icon'、'text'
    也可以同时使用多种类型组合，用'+'连接，譬如：'icon+text'  默认：'circle'.

- stroked (boolean; default True):
    设置是否针对要素中的多边形及渲染为圆圈的点要素进行轮廓绘制  默认：False.

- tooltipRenderer (string; optional):
    用于动态构造鼠标悬停tooltip内容的js函数字符串.

- visible (boolean; default True):
    设置当前图层是否可见  默认：True.

- wireframe (boolean; default False):
    extruded=True时，设置是否为进行高度拉伸的要素渲染边框  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'GeoJsonLayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, data=Component.UNDEFINED, visible=Component.UNDEFINED, opacity=Component.UNDEFINED, pickable=Component.UNDEFINED, highlightColor=Component.UNDEFINED, autoHighlight=Component.UNDEFINED, tooltipRenderer=Component.UNDEFINED, pointType=Component.UNDEFINED, filled=Component.UNDEFINED, stroked=Component.UNDEFINED, lineWidthUnits=Component.UNDEFINED, lineWidthScale=Component.UNDEFINED, lineWidthMinPixels=Component.UNDEFINED, lineWidthMaxPixels=Component.UNDEFINED, lineBillboard=Component.UNDEFINED, extruded=Component.UNDEFINED, wireframe=Component.UNDEFINED, elevationScale=Component.UNDEFINED, pointRadiusUnits=Component.UNDEFINED, pointRadiusScale=Component.UNDEFINED, pointRadiusMinPixels=Component.UNDEFINED, pointRadiusMaxPixels=Component.UNDEFINED, pointBillboard=Component.UNDEFINED, getFillColor=Component.UNDEFINED, getLineColor=Component.UNDEFINED, getLineWidth=Component.UNDEFINED, getElevation=Component.UNDEFINED, getPointRadius=Component.UNDEFINED, debounceWait=Component.UNDEFINED, hoverEvent=Component.UNDEFINED, clickEvent=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoHighlight', 'clickEvent', 'data', 'debounceWait', 'elevationScale', 'extruded', 'filled', 'getElevation', 'getFillColor', 'getLineColor', 'getLineWidth', 'getPointRadius', 'highlightColor', 'hoverEvent', 'key', 'lineBillboard', 'lineWidthMaxPixels', 'lineWidthMinPixels', 'lineWidthScale', 'lineWidthUnits', 'opacity', 'pickable', 'pointBillboard', 'pointRadiusMaxPixels', 'pointRadiusMinPixels', 'pointRadiusScale', 'pointRadiusUnits', 'pointType', 'stroked', 'tooltipRenderer', 'visible', 'wireframe']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoHighlight', 'clickEvent', 'data', 'debounceWait', 'elevationScale', 'extruded', 'filled', 'getElevation', 'getFillColor', 'getLineColor', 'getLineWidth', 'getPointRadius', 'highlightColor', 'hoverEvent', 'key', 'lineBillboard', 'lineWidthMaxPixels', 'lineWidthMinPixels', 'lineWidthScale', 'lineWidthUnits', 'opacity', 'pickable', 'pointBillboard', 'pointRadiusMaxPixels', 'pointRadiusMinPixels', 'pointRadiusScale', 'pointRadiusUnits', 'pointType', 'stroked', 'tooltipRenderer', 'visible', 'wireframe']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(GeoJsonLayer, self).__init__(**args)
