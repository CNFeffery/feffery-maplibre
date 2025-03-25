import dash
from dash import html
import feffery_maplibre as fm
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fm.MapContainer(
            initialViewState={
                "longitude": 106,
                "latitude": 29,
                "zoom": 2,
            },
            mapStyle={
                "version": 8,
                "projection": {"type": "globe"},
                "sources": {
                    "satellite": {
                        "url": "https://api.maptiler.com/tiles/satellite-v2/tiles.json?key=get_your_own_OpIi9ZULNHzrESv6T2vL",
                        "type": "raster",
                    },
                },
                "layers": [
                    {
                        "id": "Satellite",
                        "type": "raster",
                        "source": "satellite",
                    },
                ],
                "sky": {
                    "atmosphere-blend": [
                        "interpolate",
                        ["linear"],
                        ["zoom"],
                        0,
                        1,
                        5,
                        1,
                        7,
                        0,
                    ]
                },
                "light": {"anchor": "map", "position": [1.5, 90, 80]},
            },
            style=style(height="100%"),
        )
    ],
    style=style(height="100vh", background="#000"),
)

if __name__ == "__main__":
    app.run(debug=True)
