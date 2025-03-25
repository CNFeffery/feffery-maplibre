# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class GeoJsonLayer(Component):
    """A GeoJsonLayer component.


Keyword arguments:

- id (string; optional):
    用于唯一标识当前图层.

- key (string; optional):
    强制重绘当前组件时使用.

- data (list | string | dict; optional):
    为当前图层设置数据源，当传入字符串时，代表数据源对应的url地址  默认：[].

- visible (boolean; default True):
    设置当前图层是否可见  默认：True.

- beforeId (string; optional):
    可选，设置当前图层插入已有图层位置之前所对应的图层id.

- opacity (number; default 1):
    设置当前图层透明度  默认：1.

- pickable (boolean; default False):
    设置是否启用鼠标交互事件  默认：False.

- highlightColor (list; default [0, 0, 128, 128]):
    设置鼠标悬停要素高亮色  接受格式如[r, g, b, a]或[r, g, b]  默认：[0, 0, 128, 128].

- autoHighlight (boolean; default False):
    当pickable为True时有效，用于设置是否自动高亮鼠标悬停的要素  默认：False.

- tooltipRenderer (string; optional):
    用于动态构造鼠标悬停tooltip内容的js函数字符串.

- pointType (a value equal to: 'circle', 'icon', 'text'; default 'circle'):
    设置针对点要素进行渲染的类型，可选的有'circle'、'icon'、'text'
    也可以同时使用多种类型组合，用'+'连接，譬如：'icon+text'  默认：'circle'.

- filled (boolean; default True):
    设置是否针对要素中的多边形及渲染为圆圈的点要素进行填充绘制  默认：True.

- stroked (boolean; default True):
    设置是否针对要素中的多边形及渲染为圆圈的点要素进行轮廓绘制  默认：False.

- lineWidthUnits (a value equal to: 'meters', 'common', 'pixels'; default 'pixels'):
    针对线要素及其他要素的轮廓线，设置宽度值对应的单位  可选的有'meters'、'common'、'pixels'
    默认：'pixels'
    参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units.

- lineWidthScale (number; default 1):
    针对线要素及其他要素的轮廓线，设置宽度扩张系数  默认：1.

- lineWidthMinPixels (number; default 1):
    针对线要素及其他要素的轮廓线，设置线条最小显示宽度，单位：像素  默认：1.

- lineWidthMaxPixels (number; optional):
    针对线要素及其他要素的轮廓线，设置线条最大显示宽度，单位：像素  默认无限制.

- lineBillboard (boolean; default False):
    针对线要素及其他要素的轮廓线，设置线条是否随着视角变化，而始终面朝屏幕视角  默认：False.

- extruded (boolean; default False):
    针对多边形，设置是否进行高度拉伸，配合getElevation参数使用  默认：False.

- wireframe (boolean; default False):
    extruded=True时，设置是否为进行高度拉伸的要素渲染边框  默认：False.

- elevationScale (number; default 1):
    extruded为True时有效，设置高度拉伸系数  默认：1.

- pointRadiusUnits (a value equal to: 'meters', 'common', 'pixels'; default 'meters'):
    pointType='circle'时有效，设置圆圈半径对应的单位  可选的有'meters'、'common'、'pixels'
    默认：'pixels'
    参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units.

- pointRadiusScale (number; default 1):
    pointType='circle'时有效，设置圆圈半径扩张系数  默认：1.

- pointRadiusMinPixels (number; default 0):
    pointType='circle'时有效，设置圆圈最小显示半径，单位：像素  默认：1.

- pointRadiusMaxPixels (number; optional):
    pointType='circle'时有效，设置圆圈最大显示半径，单位：像素  默认无限制.

- pointBillboard (boolean; default False):
    pointType='circle'时有效，设置圆圈是否随着视角变化，而始终面朝屏幕视角  默认：False.

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

- getElevation (dict; default 1000):
    extruded=True时，针对拉伸高度的多边形，控制高度驱动方式  默认：1000.

    `getElevation` is a number | string | dict with keys:

    - func (string; optional)

- getPointRadius (dict; default 1):
    针对以圆圈形式渲染的点要素，控制圆圈半径驱动方式  默认：1.

    `getPointRadius` is a number | string | dict with keys:

    - func (string; optional)

- debounceWait (number; default 200):
    设置事件监听防抖延时，单位：毫秒  默认：200.

- hoverEvent (dict; optional):
    监听鼠标悬停事件相关参数.

- clickEvent (dict; optional):
    监听鼠标点击事件相关参数."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'GeoJsonLayer'
    GetFillColor = TypedDict(
        "GetFillColor",
            {
            "func": NotRequired[str]
        }
    )

    GetLineColor = TypedDict(
        "GetLineColor",
            {
            "func": NotRequired[str]
        }
    )

    GetLineWidth = TypedDict(
        "GetLineWidth",
            {
            "func": NotRequired[str]
        }
    )

    GetElevation = TypedDict(
        "GetElevation",
            {
            "func": NotRequired[str]
        }
    )

    GetPointRadius = TypedDict(
        "GetPointRadius",
            {
            "func": NotRequired[str]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        data: typing.Optional[typing.Union[typing.Sequence, str, dict]] = None,
        visible: typing.Optional[bool] = None,
        beforeId: typing.Optional[str] = None,
        opacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        pickable: typing.Optional[bool] = None,
        highlightColor: typing.Optional[typing.Sequence] = None,
        autoHighlight: typing.Optional[bool] = None,
        tooltipRenderer: typing.Optional[str] = None,
        pointType: typing.Optional[Literal["circle", "icon", "text"]] = None,
        filled: typing.Optional[bool] = None,
        stroked: typing.Optional[bool] = None,
        lineWidthUnits: typing.Optional[Literal["meters", "common", "pixels"]] = None,
        lineWidthScale: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        lineWidthMinPixels: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        lineWidthMaxPixels: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        lineBillboard: typing.Optional[bool] = None,
        extruded: typing.Optional[bool] = None,
        wireframe: typing.Optional[bool] = None,
        elevationScale: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        pointRadiusUnits: typing.Optional[Literal["meters", "common", "pixels"]] = None,
        pointRadiusScale: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        pointRadiusMinPixels: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        pointRadiusMaxPixels: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        pointBillboard: typing.Optional[bool] = None,
        getFillColor: typing.Optional[typing.Union[typing.Sequence, str, "GetFillColor"]] = None,
        getLineColor: typing.Optional[typing.Union[typing.Sequence, str, "GetLineColor"]] = None,
        getLineWidth: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str, "GetLineWidth"]] = None,
        getElevation: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str, "GetElevation"]] = None,
        getPointRadius: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str, "GetPointRadius"]] = None,
        debounceWait: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        hoverEvent: typing.Optional[dict] = None,
        clickEvent: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'pickable', 'highlightColor', 'autoHighlight', 'tooltipRenderer', 'pointType', 'filled', 'stroked', 'lineWidthUnits', 'lineWidthScale', 'lineWidthMinPixels', 'lineWidthMaxPixels', 'lineBillboard', 'extruded', 'wireframe', 'elevationScale', 'pointRadiusUnits', 'pointRadiusScale', 'pointRadiusMinPixels', 'pointRadiusMaxPixels', 'pointBillboard', 'getFillColor', 'getLineColor', 'getLineWidth', 'getElevation', 'getPointRadius', 'debounceWait', 'hoverEvent', 'clickEvent']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'pickable', 'highlightColor', 'autoHighlight', 'tooltipRenderer', 'pointType', 'filled', 'stroked', 'lineWidthUnits', 'lineWidthScale', 'lineWidthMinPixels', 'lineWidthMaxPixels', 'lineBillboard', 'extruded', 'wireframe', 'elevationScale', 'pointRadiusUnits', 'pointRadiusScale', 'pointRadiusMinPixels', 'pointRadiusMaxPixels', 'pointBillboard', 'getFillColor', 'getLineColor', 'getLineWidth', 'getElevation', 'getPointRadius', 'debounceWait', 'hoverEvent', 'clickEvent']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(GeoJsonLayer, self).__init__(**args)
