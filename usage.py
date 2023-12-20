import uuid
import json
import dash
import random
import feffery_maplibre as fm
from dash import Dash, html, Input, Output, State

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '执行fitBounds',
            id='execute-fit-bounds',
            style={
                'position': 'fixed',
                'zIndex': 999,
                'top': 25,
                'left': 25
            }
        ),
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                ),
                fm.ScaleControl(),
                fm.LayerGroup(
                    id='action-container'
                )
            ],
            id='demo-map',
            mapStyle='https://api.maptiler.com/maps/basic-v2/style.json?key=pctRciYXNuENsTzDTtAS',
            style={
                'height': '100%'
            }
        )
    ],
    style={
        'height': '100vh'
    }
)


@app.callback(
    Output('action-container', 'children'),
    Input('execute-fit-bounds', 'n_clicks'),
    prevent_initial_call=True
)
def execute_fit_bounds(n_clicks):

    return fm.FitBounds(
        mapActionConfig={
            'bounds': [32.958984, -5.353521, 43.50585, 5.615985],
            'duration': 0
        },
        delayAfterAction=200
    )


if __name__ == '__main__':
    app.run_server(debug=True)
