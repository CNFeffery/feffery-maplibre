if True:
    import sys
    sys.path.append('../..')

    import dash
    from dash import html
    import feffery_maplibre as fm
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyCompareSlider(
            firstItem=fm.MapContainer(
                [
                    fm.Source(
                        [
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

                    # fm.Layer(
                    #     id='background',
                    #     layerProps={
                    #         'type': 'background',
                    #         'paint': {
                    #             'background-color': '#343a40'
                    #         }
                    #     }
                    # )
                ],
                id='first-map',
                initialViewState={
                    'longitude': 106,
                    'latitude': 29,
                    'zoom': 7,
                    'pitch': 45,
                    'bearing': 45,
                },
                mapStyle='https://api.maptiler.com/maps/hybrid/style.json?key=pctRciYXNuENsTzDTtAS',
                style={
                    'height': '100%'
                }
            ),
            secondItem=fm.MapContainer(
                [
                    fm.Source(
                        [
                            fm.NavigationControl(
                                visualizePitch=True
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
                                        'line-color': '#91a7ff'
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

                    fm.Layer(
                        id='background',
                        layerProps={
                            'type': 'background',
                            'paint': {
                                'background-color': '#343a40'
                            }
                        }
                    )
                ],
                id='second-map',
                initialViewState={
                    'longitude': 106,
                    'latitude': 29,
                    'zoom': 7,
                    'pitch': 45,
                    'bearing': 45,
                },
                style={
                    'height': '100%'
                }
            ),
            style={
                'height': '100%'
            },
            boundsPadding=100,
            buttonStyle={
                'width': 32,
                'height': 32,
                # 'background': '#4dabf7'
            }
        )
    ],
    style={
        'height': '100vh'
    }
)


app.clientside_callback(
    '''(
        first_longitude,
        first_latitude,
        first_zoom,
        first_pitch,
        first_bearing,
        second_longitude,
        second_latitude,
        second_zoom,
        second_pitch,
        second_bearing
    ) => {
        if ( window.dash_clientside.callback_context.triggered[0].prop_id.startsWith('first-map') ) {
            return [
                window.dash_clientside.no_update,
                window.dash_clientside.no_update,
                window.dash_clientside.no_update,
                window.dash_clientside.no_update,
                window.dash_clientside.no_update,
                first_longitude,
                first_latitude,
                first_zoom,
                first_pitch,
                first_bearing
            ];
        }

        return [
            second_longitude,
            second_latitude,
            second_zoom,
            second_pitch,
            second_bearing,
            window.dash_clientside.no_update,
            window.dash_clientside.no_update,
            window.dash_clientside.no_update,
            window.dash_clientside.no_update,
            window.dash_clientside.no_update,
        ];
    }''',
    [Output('first-map', 'longitude'),
     Output('first-map', 'latitude'),
     Output('first-map', 'zoom'),
     Output('first-map', 'pitch'),
     Output('first-map', 'bearing'),
     Output('second-map', 'longitude'),
     Output('second-map', 'latitude'),
     Output('second-map', 'zoom'),
     Output('second-map', 'pitch'),
     Output('second-map', 'bearing'), ],
    [Input('first-map', 'longitude'),
     Input('first-map', 'latitude'),
     Input('first-map', 'zoom'),
     Input('first-map', 'pitch'),
     Input('first-map', 'bearing'),
     Input('second-map', 'longitude'),
     Input('second-map', 'latitude'),
     Input('second-map', 'zoom'),
     Input('second-map', 'pitch'),
     Input('second-map', 'bearing')],
    prevent_initial_call=True
)

if __name__ == '__main__':
    app.run(debug=True)
