# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FitBounds(Component):
    """A FitBounds component.


Keyword arguments:

- id (string; optional):
    必填，用于唯一标识当前组件.

- abortPreviousAction (boolean; default True):
    设置当上一段地图动作还未执行完成时，是否强制执行最新参数下的地图动作  默认：True.

- delay (number; optional):
    设置动作延时，单位：毫秒.

- delayAfterAction (number; default 500):
    设置在动作开始执行多少毫秒后，进行相关监听类参数的更新  默认：500.

- key (string; optional):
    强制重绘当前组件时使用.

- mapActionConfig (dict; optional):
    用于设置要执行的地图动作参数，每次有效设置后会立即执行，且当前参数会在每次有效执行完成后被重置为空.

    `mapActionConfig` is a dict with keys:

    - animate (boolean; optional):
        设置是否开启动画过渡效果.

    - bearing (number; optional):
        用于设置目标地图动作对应的地图旋转角度.

    - bounds (list; optional):
        用于设置目标地图动作对应的地图视角坐标范围  格式为[经度下限, 纬度下限, 经度上限, 纬度上限]  默认：None.

    - duration (number; optional):
        设置动画持续时长，单位：毫秒.

    - linear (boolean; optional):
        设置是否开启线性动画效果，开启后动画效果类似EaseTo，关闭后类似FlyTo  默认：False.

    - maxZoom (number; optional):
        用于设置向目标地图动作对应的bounds进行过渡时，最大允许的缩放层级.

    - padding (dict; optional):
        用于设置目标地图动作对应不同方向的像素留白大小.

        `padding` is a dict with keys:

        - bottom (number; optional):
            设置距离地图底端的像素留白大小.

        - left (number; optional):
            设置距离地图左侧的像素留白大小.

        - right (number; optional):
            设置距离地图右侧的像素留白大小.

        - top (number; optional):
            设置距离地图顶端的像素留白大小.

    - pitch (number; optional):
        用于设置目标地图动作对应的地图倾斜角度.

    - zoom (number; optional):
        用于设置目标地图动作对应的缩放级别.

- zoomAfterAction (number; optional):
    每次成功执行fitBounds动作后，监听最新的zoom级别."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_maplibre'
    _type = 'FitBounds'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, mapActionConfig=Component.UNDEFINED, delay=Component.UNDEFINED, abortPreviousAction=Component.UNDEFINED, zoomAfterAction=Component.UNDEFINED, delayAfterAction=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'abortPreviousAction', 'delay', 'delayAfterAction', 'key', 'mapActionConfig', 'zoomAfterAction']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'abortPreviousAction', 'delay', 'delayAfterAction', 'key', 'mapActionConfig', 'zoomAfterAction']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FitBounds, self).__init__(**args)
