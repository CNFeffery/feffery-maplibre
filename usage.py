import uuid
import json
import dash
import random
import feffery_maplibre as fm
from dash import Dash, html, Input, Output, State

app = Dash(__name__)

app.layout = html.Div(
    [
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                ),
                fm.ScaleControl()
            ],
            debug=True,
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


if __name__ == '__main__':
    app.run_server(debug=True)
