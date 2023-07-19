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
        fuc.FefferyResizable(
            fm.MapContainer(
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
                    )
                ],
                initialViewState={
                    'longitude': 106,
                    'latitude': 29,
                    'zoom': 7,
                    'pitch': 45,
                    'bearing': 45,
                },
                mapStyle='https://api.maptiler.com/maps/hybrid/style.json?key=pctRciYXNuENsTzDTtAS',
                style={
                    'height': '100%',
                    'width': '100%'
                }
            ),
            defaultSize={
                'width': 600,
                'height': 600
            }
        )
    ],
    style={
        'height': '100vh'
    }
)


if __name__ == '__main__':
    app.run(debug=True, port=8002)
