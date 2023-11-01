if True:
    import sys
    sys.path.append('../..')

    import dash
    import json
    from dash import html
    import feffery_maplibre as fm
    from dash.dependencies import Input, Output, ALL

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Button(
                    '清空已绘制要素',
                    id='delete-all-test'
                ),
                html.Button(
                    '删除已选要素',
                    id='delete-selected-test'
                ),
                html.Button(
                    'simple_select',
                    id={
                        'type': 'mode-change',
                        'mode': 'simple_select'
                    }
                ),
                html.Button(
                    'draw_line_string',
                    id={
                        'type': 'mode-change',
                        'mode': 'draw_line_string'
                    }
                ),
                html.Button(
                    'draw_polygon',
                    id={
                        'type': 'mode-change',
                        'mode': 'draw_polygon'
                    }
                ),
                html.Button(
                    'draw_point',
                    id={
                        'type': 'mode-change',
                        'mode': 'draw_point'
                    }
                ),
                html.Button(
                    'draw_circle',
                    id={
                        'type': 'mode-change',
                        'mode': 'draw_circle'
                    }
                ),
                html.Button(
                    'freehand_polygon',
                    id={
                        'type': 'mode-change',
                        'mode': 'freehand_polygon'
                    }
                )
            ]
        ),
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                ),
                # 调用esri开放影像底图
                fm.Source(
                    [
                        fm.Layer(
                            id='img-layer',
                            layerProps={
                                'type': 'raster',
                                'source': 'img-source'
                            }
                        )
                    ],
                    id='img-source',
                    sourceProps={
                        'type': 'raster',
                        'tiles': [
                            'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        ],
                        'tileSize': 256
                    }
                ),
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
            ],
            id='map-demo',
            enableDraw=True,
            # drawOnlyOne=True,
            drawCircleSteps=128,
            drawControls={
                'point': False,
                'line_string': False,
                'polygon': False,
                'trash': False
            },
            drawSpatialJudgeListenLayerIds=[
                'mapbox-demo-layer-landuse',
                'mapbox-demo-country_label',
                'mapbox-demo-admin',
                'mapbox-demo-water',
                'mapbox-demo-road',
            ],
            enableDrawSpatialJudge=True,
            style={
                'width': '100%',
                'height': '50%'
            }
        ),
        html.Pre(id='map-demo-output')
    ],
    style={
        'height': '100vh'
    }
)


@app.callback(
    Output('map-demo-output', 'children'),
    [Input('map-demo', 'drawnFeatures'),
     Input('map-demo', 'currentDrawMode')],
    prevent_initial_call=True
)
def show_current_drawnFeatures(drawnFeatures, currentDrawMode):

    return json.dumps(
        dict(
            currentDrawMode=currentDrawMode,
            drawnFeatures=[
                {
                    'id': feature['id'],
                    'properties': feature['properties']
                }
                for feature in drawnFeatures
            ]
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('map-demo', 'drawDeleteAll'),
    Input('delete-all-test', 'n_clicks'),
    prevent_initial_call=True
)
def delete_all_test(n_clicks):

    return True


@app.callback(
    Output('map-demo', 'drawDeleteSelected'),
    Input('delete-selected-test', 'n_clicks'),
    prevent_initial_call=True
)
def delete_selected_test(n_clicks):

    return True


@app.callback(
    Output('map-demo', 'setDrawMode'),
    Input(
        {
            'type': 'mode-change',
            'mode': ALL
        },
        'n_clicks'
    ),
    prevent_initial_call=True
)
def handle_mode_change(_):

    return dash.ctx.triggered_id['mode']


if __name__ == '__main__':
    app.run(debug=True, port=8050)
