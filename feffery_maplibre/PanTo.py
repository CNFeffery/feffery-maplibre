# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PanTo(Component):
    """A PanTo component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- abortPreviousAction (boolean; default True):
    设置当上一段地图动作还未执行完成时，是否强制执行最新参数下的地图动作  默认：True.

- delay (number; optional):
    设置动作延时，单位：毫秒.

- key (string; optional):
    强制重绘当前组件时使用.

- mapActionConfig (dict; optional):
    用于设置要执行的地图动作参数，每次有效设置后会立即执行，且当前参数会在每次有效执行完成后被重置为空.

    `mapActionConfig` is a dict with keys:

    - animate (boolean; optional):
        设置是否开启动画过渡效果.

    - duration (number; optional):
        设置动画持续时长，单位：毫秒.

    - lnglat (list of numbers; optional):
        用于设置目标地图动作对应的目标点坐标，格式如[目标经度, 目标纬度]."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'PanTo'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, mapActionConfig=Component.UNDEFINED, delay=Component.UNDEFINED, abortPreviousAction=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'abortPreviousAction', 'delay', 'key', 'mapActionConfig']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'abortPreviousAction', 'delay', 'key', 'mapActionConfig']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(PanTo, self).__init__(**args)
