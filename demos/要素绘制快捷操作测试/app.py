if True:
    import sys
    sys.path.append('../..')

    import dash
    import json
    from dash import html
    import feffery_maplibre as fm
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Button(
                    '清空已绘制要素',
                    id='delete-all-test'
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
            drawOnlyOne=True,
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
    Input('map-demo', 'drawnFeatures'),
    prevent_initial_call=True
)
def show_current_drawnFeatures(drawnFeatures):

    return json.dumps(
        dict(
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


if __name__ == '__main__':
    app.run(debug=True, port=8050)
