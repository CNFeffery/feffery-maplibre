import feffery_maplibre as fm
from dash import Dash, html

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
                ),
                fm.GeolocateControl(
                    position='top-left',
                    # positionOptions={
                    #     'enableHighAccuracy': True
                    # },
                    showUserHeading=True,
                    trackUserLocation=True
                )
            ],
            mapStyle='https://api.maptiler.com/maps/satellite/style.json?key=pctRciYXNuENsTzDTtAS',
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
    app.run_server(debug=True, host='0.0.0.0')
