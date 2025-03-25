# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class ArcLayer(Component):
    """An ArcLayer component.


Keyword arguments:

- id (string; optional):
    用于唯一标识当前图层.

- key (string; optional):
    强制重绘当前组件时使用.

- data (list | string; optional):
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

- greatCircle (boolean; default False):
    是否启用大圆弧线模式  默认：False.

- numSegments (number; default 50):
    设置每段弧线的分段数量，越大弧线越接近曲线  默认：50.

- widthUnits (a value equal to: 'meters', 'common', 'pixels'; default 'pixels'):
    设置宽度单位，可选的有'meters'、'common'、'pixels'  默认：'pixels'
    参考资料：https://deck.gl/docs/developer-guide/coordinate-systems#supported-units.

- widthScale (number; default 1):
    设置宽度扩张系数  默认：1.

- widthMinPixels (number; default 1):
    设置弧线最小显示宽度，单位：像素  默认：1.

- widthMaxPixels (number; optional):
    设置弧线最大显示宽度，单位：像素  默认无限制.

- getSourcePosition (dict; optional):
    控制弧线起点坐标驱动方式.

    `getSourcePosition` is a string | dict with keys:

    - func (string; optional)

- getTargetPosition (dict; optional):
    控制弧线终点坐标驱动方式.

    `getTargetPosition` is a string | dict with keys:

    - func (string; optional)

- getSourceColor (list of dicts; optional):
    控制弧线起点颜色驱动方式.

    `getSourceColor` is a list | string | dict with keys:

    - func (string; optional)

- getTargetColor (list of dicts; optional):
    控制弧线终点颜色驱动方式.

    `getTargetColor` is a list | string | dict with keys:

    - func (string; optional)

- getWidth (dict; optional):
    控制弧线宽度驱动方式.

    `getWidth` is a number | string | dict with keys:

    - func (string; optional)

- getHeight (dict; optional):
    控制弧线高度系数驱动方式.

    `getHeight` is a number | string | dict with keys:

    - func (string; optional)

- getTilt (dict; optional):
    控制弧线微调系数驱动方式，用于解决相同起点终点的多条弧线相互重叠的问题  参数值应在-90到90之间，单位：度.

    `getTilt` is a number | string | dict with keys:

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
    _type = 'ArcLayer'
    GetSourcePosition = TypedDict(
        "GetSourcePosition",
            {
            "func": NotRequired[str]
        }
    )

    GetTargetPosition = TypedDict(
        "GetTargetPosition",
            {
            "func": NotRequired[str]
        }
    )

    GetSourceColor = TypedDict(
        "GetSourceColor",
            {
            "func": NotRequired[str]
        }
    )

    GetTargetColor = TypedDict(
        "GetTargetColor",
            {
            "func": NotRequired[str]
        }
    )

    GetWidth = TypedDict(
        "GetWidth",
            {
            "func": NotRequired[str]
        }
    )

    GetHeight = TypedDict(
        "GetHeight",
            {
            "func": NotRequired[str]
        }
    )

    GetTilt = TypedDict(
        "GetTilt",
            {
            "func": NotRequired[str]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        data: typing.Optional[typing.Union[typing.Sequence, str]] = None,
        visible: typing.Optional[bool] = None,
        beforeId: typing.Optional[str] = None,
        opacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        pickable: typing.Optional[bool] = None,
        highlightColor: typing.Optional[typing.Sequence] = None,
        autoHighlight: typing.Optional[bool] = None,
        tooltipRenderer: typing.Optional[str] = None,
        greatCircle: typing.Optional[bool] = None,
        numSegments: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        widthUnits: typing.Optional[Literal["meters", "common", "pixels"]] = None,
        widthScale: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        widthMinPixels: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        widthMaxPixels: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        getSourcePosition: typing.Optional[typing.Union[str, "GetSourcePosition"]] = None,
        getTargetPosition: typing.Optional[typing.Union[str, "GetTargetPosition"]] = None,
        getSourceColor: typing.Optional[typing.Union[typing.Sequence, str, "GetSourceColor"]] = None,
        getTargetColor: typing.Optional[typing.Union[typing.Sequence, str, "GetTargetColor"]] = None,
        getWidth: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str, "GetWidth"]] = None,
        getHeight: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str, "GetHeight"]] = None,
        getTilt: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str, "GetTilt"]] = None,
        debounceWait: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        hoverEvent: typing.Optional[dict] = None,
        clickEvent: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'pickable', 'highlightColor', 'autoHighlight', 'tooltipRenderer', 'greatCircle', 'numSegments', 'widthUnits', 'widthScale', 'widthMinPixels', 'widthMaxPixels', 'getSourcePosition', 'getTargetPosition', 'getSourceColor', 'getTargetColor', 'getWidth', 'getHeight', 'getTilt', 'debounceWait', 'hoverEvent', 'clickEvent']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'data', 'visible', 'beforeId', 'opacity', 'pickable', 'highlightColor', 'autoHighlight', 'tooltipRenderer', 'greatCircle', 'numSegments', 'widthUnits', 'widthScale', 'widthMinPixels', 'widthMaxPixels', 'getSourcePosition', 'getTargetPosition', 'getSourceColor', 'getTargetColor', 'getWidth', 'getHeight', 'getTilt', 'debounceWait', 'hoverEvent', 'clickEvent']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ArcLayer, self).__init__(**args)
