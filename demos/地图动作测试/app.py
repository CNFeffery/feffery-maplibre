if True:
    import sys
    sys.path.append('../..')

    import dash
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
                html.Button(
                    '随机EaseTo',
                    id='random-ease-to'
                ),
                html.Button(
                    'FitBounds示例',
                    id='fit-bounds-demo'
                ),
                html.Button(
                    '随机FlyTo',
                    id='random-fly-to'
                ),
                html.Button(
                    '随机JumpTo',
                    id='random-jump-to'
                ),
                html.Button(
                    '随机PanBy',
                    id='random-pan-by'
                ),
                html.Button(
                    '随机PanTo',
                    id='random-pan-to'
                ),
                html.Button(
                    '随机RotateTo',
                    id='random-rotate-to'
                ),
                html.Button(
                    'ZoomIn示例',
                    id='zoom-in-demo'
                ),
                html.Button(
                    'ZoomOut示例',
                    id='zoom-out-demo'
                ),
                html.Button(
                    '随机ZoomTo',
                    id='random-zoom-to'
                ),
            ]
        ),
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                ),
                fm.ScaleControl(),

                html.Div(
                    id='map-action-demo'
                )
            ],
            id='map-demo',
            mapStyle='https://api.maptiler.com/maps/hybrid/style.json?key=pctRciYXNuENsTzDTtAS',
            style={
                'width': '100%',
                'height': 'calc(100vh - 23px)'
            }
        )
    ],
    style={
        'height': '100vh'
    }
)


@app.callback(
    Output('map-action-demo', 'children'),
    Input('random-ease-to', 'n_clicks'),
    prevent_initial_call=True
)
def random_ease_to(n_clicks):

    return fm.EaseTo(
        mapActionConfig={
            'center': [random.uniform(-180, 180), random.uniform(-90, 90)],
            'zoom': random.randint(2, 6),
            'duration': random.uniform(1000, 3000)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('fit-bounds-demo', 'n_clicks'),
    prevent_initial_call=True
)
def fit_bounds_demo(n_clicks):

    return fm.FitBounds(
        mapActionConfig={
            'bounds': [32.958984, -5.353521, 43.50585, 5.615985],
            'duration': 3000
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('random-fly-to', 'n_clicks'),
    prevent_initial_call=True
)
def random_fly_to(n_clicks):

    return fm.FlyTo(
        mapActionConfig={
            'center': [random.uniform(-180, 180), random.uniform(-90, 90)],
            'zoom': random.randint(2, 6),
            'duration': random.uniform(1000, 3000)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('random-jump-to', 'n_clicks'),
    prevent_initial_call=True
)
def random_jump_to(n_clicks):

    return fm.JumpTo(
        mapActionConfig={
            'center': [random.uniform(-180, 180), random.uniform(-90, 90)],
            'zoom': random.randint(2, 6)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('random-pan-by', 'n_clicks'),
    prevent_initial_call=True
)
def random_pan_by(n_clicks):

    return fm.PanBy(
        mapActionConfig={
            'offset': [random.uniform(-100, 100), random.uniform(-100, 100)],
            'duration': random.uniform(1000, 3000)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('random-pan-to', 'n_clicks'),
    prevent_initial_call=True
)
def random_pan_to(n_clicks):

    return fm.PanTo(
        mapActionConfig={
            'lnglat': [random.uniform(-180, 180), random.uniform(-90, 90)],
            'duration': random.uniform(1000, 3000)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('random-rotate-to', 'n_clicks'),
    prevent_initial_call=True
)
def random_rotate_to(n_clicks):

    return fm.RotateTo(
        mapActionConfig={
            'bearing': random.uniform(0, 360),
            'duration': random.uniform(1000, 3000)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('zoom-in-demo', 'n_clicks'),
    prevent_initial_call=True
)
def zoom_in_demo(n_clicks):

    return fm.ZoomIn(
        mapActionConfig={
            'duration': random.uniform(1000, 3000)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('zoom-out-demo', 'n_clicks'),
    prevent_initial_call=True
)
def zoom_out_demo(n_clicks):

    return fm.ZoomOut(
        mapActionConfig={
            'duration': random.uniform(1000, 3000)
        }
    )


@app.callback(
    Output('map-action-demo', 'children', allow_duplicate=True),
    Input('random-zoom-to', 'n_clicks'),
    prevent_initial_call=True
)
def random_zoom_to(n_clicks):

    return fm.ZoomTo(
        mapActionConfig={
            'zoom': random.uniform(0, 18),
            'duration': random.uniform(1000, 3000)
        }
    )


if __name__ == '__main__':
    app.run(debug=True, port=8003)
