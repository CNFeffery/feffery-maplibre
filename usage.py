import uuid
import json
import dash
import random
import feffery_maplibre as fm
from dash import Dash, html, Input, Output, State

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                fm.MapContainer(
                    [
                        fm.NavigationControl(
                            visualizePitch=True
                        ),
                        fm.ScaleControl(),

                        fm.Source(
                            [
                                fm.Layer(
                                    id='mapbox-demo-layer-landuse',
                                    layerProps={
                                        'source-layer': 'landuse',
                                        'type': 'fill',
                                        'paint':  {
                                            'fill-color': 'green',
                                            'fill-opacity': 0.4,
                                            'fill-outline-color': 'green'
                                        }
                                    },
                                    hoverCursor='pointer'
                                ),
                                fm.Layer(
                                    id='mapbox-demo-country_label',
                                    layerProps={
                                        'source-layer': 'country_label',
                                        'type': 'circle'
                                    },
                                    hoverCursor='pointer'
                                ),
                                fm.Layer(
                                    id='mapbox-demo-admin',
                                    layerProps={
                                        'source-layer': 'admin',
                                        'type': 'fill',
                                        'paint': {
                                            'fill-outline-color': '#faa2c1',
                                            'fill-opacity': 0
                                        }
                                    },
                                    hoverCursor='pointer'
                                ),
                                fm.Layer(
                                    id='mapbox-demo-water',
                                    layerProps={
                                        'source-layer': 'water',
                                        'type': 'fill',
                                        'paint': {
                                            'fill-color': '#c5f6fa'
                                        }
                                    },
                                    hoverCursor='pointer'
                                ),
                                fm.Layer(
                                    id='mapbox-demo-road',
                                    layerProps={
                                        'source-layer': 'road',
                                        'type': 'line',
                                        'paint': {
                                            'line-color': '#fab005'
                                        }
                                    },
                                    hoverCursor='pointer'
                                )
                            ],
                            id='mapbox-demo-source',
                            sourceProps={
                                'tiles':  [
                                    'https://b.tiles.mapbox.com/v4/mapbox.mapbox-streets-v6/{z}/{x}/{y}.vector.pbf?sku=101SPH62Z4zzs&access_token=pk.eyJ1IjoiZmVmZmVyeXB6eSIsImEiOiJjanhyY2QyenUwN2VzM2x0NWh6MGVzOWFqIn0.Z2HEVP_nJ8Smx_IWxkdRqg'
                                ],
                                'type': 'vector'
                            }
                        ),

                        # fm.Source(
                        #     [
                        #         fm.Layer(
                        #             id='demo-layer',
                        #             layerProps={
                        #                 'source-layer': 'dt860',
                        #                 'type': 'fill',
                        #                 'paint': {
                        #                     'fill-color': '#81ecec',
                        #                     'fill-opacity': 0.4,
                        #                     'fill-outline-color': 'black'
                        #                 }
                        #             },
                        #             hoverCursor='pointer'
                        #         )
                        #     ],
                        #     id='demo-source',
                        #     sourceProps={
                        #         'tiles': [
                        #             'http://10.10.0.26:9101/mapserver/tms/1.0.0/cu:dt860@EPSG:900913@pbf/{z}/{x}/{y}.pbf'
                        #         ],
                        #         'type': 'vector',
                        #         'scheme': 'tms'
                        #     }
                        # )
                    ],
                    id='map-demo',
                    # mapStyle='https://api.maptiler.com/maps/basic-v2/style.json?key=pctRciYXNuENsTzDTtAS',
                    initialViewState={
                        'longitude': 106,
                        'latitude': 29,
                        'zoom': 7,
                        'pitch': 45,
                        'bearing': 45,
                    },
                    clickListenLayerIds=[
                        'mapbox-demo-layer-landuse',
                        'mapbox-demo-country_label',
                        'mapbox-demo-admin',
                        'mapbox-demo-water',
                        'mapbox-demo-road',
                    ],
                    clickListenBoxSize=5,
                    debounceWait=200,
                    boxZoom=True,
                    locale={
                        'NavigationControl.ZoomIn': '放大地图',
                        'NavigationControl.ZoomOut': '缩小地图',
                        'NavigationControl.ResetBearing': '重置地图角度'
                    },
                    style={
                        'width': '100%',
                        'height': 'calc(100% - 40px)'
                    },
                    enableDraw=True,
                    drawOnlyOne=True,
                    enableDrawSpatialJudge=True,
                    drawSpatialJudgeListenLayerIds=[
                        'mapbox-demo-layer-landuse',
                        'mapbox-demo-country_label',
                        'mapbox-demo-admin',
                        'mapbox-demo-water',
                        'mapbox-demo-road',
                    ],
                    drawSpatialJudgePredicate='contains'
                    # enableDeckGL=True
                ),
                html.Div(
                    [
                        html.Button(
                            'longitude=>0',
                            id='set-longitude-0'
                        ),
                        html.Button(
                            '清除测试图层',
                            id='clear-demo-layers'
                        ),
                        html.Button(
                            '添加测试图层',
                            id='add-demo-layers'
                        ),
                        html.Button(
                            '更新图层样式',
                            id='update-demo-layers-style'
                        ),
                        html.Button(
                            '打乱图层顺序',
                            id='shuffle-demo-layers-style'
                        )
                    ]
                )
            ],
            style={
                'flex': 2
            }
        ),
        html.Div(
            html.Pre(
                id='test-props',
                style={
                    'height': 'calc(100vh - 20px)',
                    'overflow': 'auto',
                    'maxWidth': '33.333vw'
                }
            ),
            style={
                'flex': 1
            }
        )
    ],
    style={
        'display': 'flex',
        'height': '100vh'
    }
)


@app.callback(
    Output('test-props', 'children'),
    [
        Input('map-demo', 'longitudeDebounce'),
        Input('map-demo', 'latitudeDebounce'),
        Input('map-demo', 'zoomDebounce'),
        Input('map-demo', 'pitchDebounce'),
        Input('map-demo', 'bearingDebounce'),
        Input('map-demo', 'clickedLngLat'),
        Input('map-demo', 'clickListenLayerFeatures'),
        Input('map-demo', 'loadedSources'),
        Input('map-demo', 'loadedLayers'),
        Input('map-demo', 'drawnFeatures'),
        Input('map-demo', 'drawSpatialJudgeListenLayerFeatures'),
    ]
)
def show_test_props(longitudeDebounce,
                    latitudeDebounce,
                    zoomDebounce,
                    pitchDebounce,
                    bearingDebounce,
                    clickedLngLat,
                    clickListenLayerFeatures,
                    loadedSources,
                    loadedLayers,
                    drawnFeatures,
                    drawSpatialJudgeListenLayerFeatures):

    return json.dumps(
        dict(
            longitudeDebounce=longitudeDebounce,
            latitudeDebounce=latitudeDebounce,
            zoomDebounce=zoomDebounce,
            pitchDebounce=pitchDebounce,
            bearingDebounce=bearingDebounce,
            clickedLngLat=clickedLngLat,
            clickListenLayerFeatures=clickListenLayerFeatures,
            loadedSources=loadedSources,
            loadedLayers=loadedLayers,
            drawnFeatures=drawnFeatures,
            drawSpatialJudgeListenLayerFeatures=drawSpatialJudgeListenLayerFeatures
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    [Output('map-demo', 'longitude'),
     Output('map-demo', 'longitudeDebounce')],
    Input('set-longitude-0', 'n_clicks'),
    prevent_initial_call=True
)
def set_longitude_0(n_clicks):

    return 0, 0


@app.callback(
    Output('mapbox-demo-source', 'children'),
    Input('clear-demo-layers', 'n_clicks'),
    prevent_initial_call=True
)
def clear_demo_source(n_clicks):

    return []


@app.callback(
    Output('mapbox-demo-source', 'children', allow_duplicate=True),
    Input('add-demo-layers', 'n_clicks'),
    prevent_initial_call=True
)
def add_demo_source(n_clicks):

    return [
        fm.Layer(
            id='mapbox-demo-layer-landuse',
            layerProps={
                'source-layer': 'landuse',
                'type': 'fill',
                'paint':  {
                    'fill-color': 'green',
                    'fill-opacity': 0.4,
                    'fill-outline-color': 'green'
                }
            },
            hoverCursor='pointer'
        ),
        fm.Layer(
            id='mapbox-demo-country_label',
            layerProps={
                'source-layer': 'country_label',
                'type': 'circle'
            },
            hoverCursor='pointer'
        )
    ]


@app.callback(
    Output('mapbox-demo-layer-landuse', 'layerProps'),
    Input('update-demo-layers-style', 'n_clicks'),
    State('mapbox-demo-layer-landuse', 'layerProps'),
    prevent_initial_call=True
)
def update_demo_layer_style(n_clicks, layerProps):

    return {
        **layerProps,
        'paint': {
            'fill-color': 'yellow',
            'fill-opacity': 0.4,
            'fill-outline-color': 'purple'
        }
    }


@app.callback(
    Output('mapbox-demo-source', 'children', allow_duplicate=True),
    Input('shuffle-demo-layers-style', 'n_clicks'),
    prevent_initial_call=True
)
def shuffle_demo_layers_style(n_clicks):

    new_layers = [
        fm.Layer(
            key=str(uuid.uuid4()),
            id='mapbox-demo-layer-landuse',
            layerProps={
                'source-layer': 'landuse',
                'type': 'fill',
                'paint':  {
                    'fill-color': 'green',
                    'fill-opacity': 0.4,
                    'fill-outline-color': 'green'
                }
            },
            hoverCursor='pointer'
        ),
        fm.Layer(
            key=str(uuid.uuid4()),
            id='mapbox-demo-country_label',
            layerProps={
                'source-layer': 'country_label',
                'type': 'circle'
            },
            hoverCursor='pointer'
        ),
        fm.Layer(
            key=str(uuid.uuid4()),
            id='mapbox-demo-admin',
            layerProps={
                'source-layer': 'admin',
                'type': 'fill',
                'paint': {
                    'fill-outline-color': '#faa2c1',
                    'fill-opacity': 0
                }
            },
            hoverCursor='pointer'
        ),
        fm.Layer(
            key=str(uuid.uuid4()),
            id='mapbox-demo-water',
            layerProps={
                'source-layer': 'water',
                'type': 'fill',
                'paint': {
                    'fill-color': '#c5f6fa'
                }
            },
            hoverCursor='pointer'
        ),
        fm.Layer(
            key=str(uuid.uuid4()),
            id='mapbox-demo-road',
            layerProps={
                'source-layer': 'road',
                'type': 'line',
                'paint': {
                    'line-color': '#fab005'
                }
            },
            hoverCursor='pointer'
        )
    ]

    # 打乱顺序
    random.shuffle(new_layers)

    return new_layers


if __name__ == '__main__':
    app.run_server(debug=True)
