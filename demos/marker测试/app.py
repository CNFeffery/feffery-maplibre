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
        fm.MapContainer(
            [
                fm.Marker(
                    # html.Span(
                    #     '测试',
                    #     style={
                    #         'fontSize': 50,
                    #         'color': 'white'
                    #     }
                    # ),
                    latitude=0,
                    longitude=0,
                    color='#ff6b6b',
                    draggable=True
                )
            ],
            initialViewState={
                'longitude': 0,
                'latitude': 0,
                'zoom': 3,
                'pitch': 0,
                'bearing': 0,
            },
            mapStyle='https://api.maptiler.com/maps/hybrid/style.json?key=pctRciYXNuENsTzDTtAS',
            style={
                'height': '100%'
            }
        )
    ],
    style={
        'height': '100vh'
    }
)


if __name__ == '__main__':
    app.run(debug=True, port=8002)
