/* eslint-disable import/prefer-default-export */
import MapContainer from './components/MapContainer.react';
// 控件类型
import AttributionControl from './components/controls/AttributionControl.react';
import FullscreenControl from './components/controls/FullscreenControl.react';
import GeolocateControl from './components/controls/GeolocateControl.react';
import NavigationControl from './components/controls/NavigationControl.react';
import ScaleControl from './components/controls/ScaleControl.react';
// 图层源
import Source from './components/sources/Source.react';
// 图层
import Layer from './components/layers/Layer.react';
// 组容器
import SourceGroup from './components/groups/SourceGroup.react';
import LayerGroup from './components/groups/LayerGroup.react';
// 工具组件
import HandleRawMap from './components/utils/HandleRawMap.react';
import SortLayers from './components/utils/SortLayers.react';
import AddImages from './components/utils/AddImages.react';
import Fragment from './components/utils/Fragment.react';
// 地图动作
import EaseTo from './components/actions/EaseTo.react';
import FitBounds from './components/actions/FitBounds.react';
import FlyTo from './components/actions/FlyTo.react';
import JumpTo from './components/actions/JumpTo.react';
import PanBy from './components/actions/PanBy.react';
import PanTo from './components/actions/PanTo.react';
import RotateTo from './components/actions/RotateTo.react';
import ZoomIn from './components/actions/ZoomIn.react';
import ZoomOut from './components/actions/ZoomOut.react';
import ZoomTo from './components/actions/ZoomTo.react';
import Resize from './components/actions/Resize.react';
import Stop from './components/actions/Stop.react';
// 其他
import Marker from './components/others/Marker.react';
import Popup from './components/others/Popup.react';
// deck.gl图层
import ArcLayer from './components/deckLayers/ArcLayer.react';
import GeoJsonLayer from './components/deckLayers/GeoJsonLayer.react';
import TerrainLayer from './components/deckLayers/TerrainLayer.react';
import HeatmapLayer from './components/deckLayers/HeatmapLayer.react';

export {
    MapContainer,
    AttributionControl,
    FullscreenControl,
    GeolocateControl,
    NavigationControl,
    ScaleControl,
    Source,
    Layer,
    SourceGroup,
    LayerGroup,
    HandleRawMap,
    SortLayers,
    AddImages,
    Fragment,
    EaseTo,
    FitBounds,
    FlyTo,
    JumpTo,
    PanBy,
    PanTo,
    RotateTo,
    ZoomIn,
    ZoomOut,
    ZoomTo,
    Resize,
    Stop,
    Marker,
    Popup,
    ArcLayer,
    GeoJsonLayer,
    TerrainLayer,
    HeatmapLayer
};