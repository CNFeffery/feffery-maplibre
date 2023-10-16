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
                )
            ]
        ),
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                )
            ],
            id='map-demo',
            mapStyle='https://api.maptiler.com/maps/hybrid/style.json?key=pctRciYXNuENsTzDTtAS',
            enableDraw=True,
            # drawOnlyOne=True,
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
            drawnFeatures=drawnFeatures
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
