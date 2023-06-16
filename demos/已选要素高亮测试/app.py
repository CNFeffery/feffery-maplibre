if True:
    import sys
    sys.path.append('../..')

    import dash
    import json
    import uuid
    import random
    from dash import html
    import feffery_maplibre as fm
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

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

                        fm.SourceGroup(
                            id='highlight-geojson-source-group'
                        )
                    ],
                    id='demo-map',
                    initialViewState={
                        'longitude': 106,
                        'latitude': 29,
                        'zoom': 7,
                        'pitch': 45,
                        'bearing': 45,
                    },
                    enableDraw=True,
                    drawOnlyOne=True,
                    enableDrawSpatialJudge=True,
                    drawControls={
                        'point': False,
                        'line_string': False
                    },
                    clickListenLayerIds=[
                        'mapbox-demo-layer-landuse',
                        'mapbox-demo-country_label',
                        'mapbox-demo-admin',
                        'mapbox-demo-water',
                        'mapbox-demo-road',
                    ],
                    drawSpatialJudgeListenLayerIds=[
                        'mapbox-demo-layer-landuse',
                        'mapbox-demo-country_label',
                        'mapbox-demo-admin',
                        'mapbox-demo-water',
                        'mapbox-demo-road',
                    ],
                    style={
                        'width': '100%',
                        'height': '100vh'
                    }
                )
            ],
            style={
                'flex': 'auto'
            }
        ),

        html.Div(
            [
                html.Pre(
                    id='demo-selected-features'
                )
            ],
            style={
                'flex': 'none',
                'width': 400
            }
        )
    ],
    style={
        'height': '100vh',
        'display': 'flex'
    }
)


# @app.callback(
#     [Output('demo-selected-features', 'children'),
#     Output('highlight-geojson-source-group', 'children')],
#     Input('demo-map', 'clickListenLayerFeatures')
# )
# def listen_clickListenLayerFeatures(clickListenLayerFeatures):

#     clickListenLayerFeatures = clickListenLayerFeatures or []

#     return [
#         json.dumps(
#             clickListenLayerFeatures,
#             indent=4,
#             ensure_ascii=False
#         ),
#         fm.Source(
#             [
#                 fm.Layer(
#                     id='highlight-geojson-layer',
#                     key=str(uuid.uuid4()),
#                     layerProps={
#                         'type': 'fill',
#                         'source': 'highlight-geojson-source',
#                         'paint': {
#                             'fill-color': '#f03e3e'
#                         }
#                     }
#                 )
#             ],
#             id='highlight-geojson-source',
#             sourceProps={
#                 'type': 'geojson',
#                 'data': {
#                     'type': 'FeatureCollection',
#                     'features': [
#                         {
#                             'type': 'Feature',
#                             'geometry': g['geometry']
#                         }
#                         for g in clickListenLayerFeatures
#                     ]
#                 }
#             }
#         )
#     ]


@app.callback(
    Output('highlight-geojson-source-group', 'children', allow_duplicate=True),
    Input('demo-map', 'drawSpatialJudgeListenLayerFeatures'),
    prevent_initial_call=True
)
def listen_drawSpatialJudgeListenLayerFeatures(drawSpatialJudgeListenLayerFeatures):

    drawSpatialJudgeListenLayerFeatures = drawSpatialJudgeListenLayerFeatures or []

    return [
        fm.Source(
            [
                fm.Layer(
                    id='highlight-geojson-layer-polygon',
                    key=str(uuid.uuid4()),
                    layerProps={
                        'type': 'fill',
                        'source': 'highlight-geojson-source',
                        'paint': {
                            'fill-color': '#f03e3e',
                            'fill-opacity': 0.6
                        }
                    }
                )
            ],
            id='highlight-geojson-source-polygon',
            sourceProps={
                'type': 'geojson',
                'data': {
                    'type': 'FeatureCollection',
                    'features': [
                        {
                            'type': 'Feature',
                            'geometry': g['_geometry']
                        }
                        for g in drawSpatialJudgeListenLayerFeatures
                        if 'polygon' in g['_geometry']['type'].lower()
                    ]
                }
            }
        ),

        fm.Source(
            [
                fm.Layer(
                    id='highlight-geojson-layer-linestring',
                    key=str(uuid.uuid4()),
                    layerProps={
                        'type': 'line',
                        'source': 'highlight-geojson-source',
                        'paint': {
                            'line-color': '#f03e3e'
                        }
                    }
                )
            ],
            id='highlight-geojson-source-linestring',
            sourceProps={
                'type': 'geojson',
                'data': {
                    'type': 'FeatureCollection',
                    'features': [
                        {
                            'type': 'Feature',
                            'geometry': g['_geometry']
                        }
                        for g in drawSpatialJudgeListenLayerFeatures
                        if 'line' in g['_geometry']['type'].lower()
                    ]
                }
            }
        )
    ]


if __name__ == '__main__':
    app.run(debug=True, port=8004)
