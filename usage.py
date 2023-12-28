import feffery_maplibre as fm
from dash import Dash, html, Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True,
                    showCompass=True,
                    position='top-left',
                ),
                fm.FullscreenControl(
                    position='top-left',
                    style={
                        'color': 'red'
                    }
                )
            ],
            # mapStyle='https://api.maptiler.com/maps/basic-v2/style.json?key=pctRciYXNuENsTzDTtAS',
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
