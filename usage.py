import json
from dash import Dash, html
import feffery_maplibre as fm
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
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
                        id='geolocate-demo',
                        position='top-left',
                        # positionOptions={
                        #     'enableHighAccuracy': True
                        # },
                        # showUserHeading=True,
                        # trackUserLocation=True
                    )
                ],
                mapStyle='https://api.maptiler.com/maps/satellite/style.json?key=pctRciYXNuENsTzDTtAS',
                # mapStyle='https://api.maptiler.com/maps/basic-v2/style.json?key=pctRciYXNuENsTzDTtAS',
                style={
                    'height': '100%'
                }
            ),
            style={
                'flex': '4'
            }
        ),
        html.Div(
            html.Pre(
                id='geolocate-info'
            ),
            style={
                'flex': '1'
            }
        )
    ],
    style={
        'height': '100vh',
        'display': 'flex'
    }
)


@app.callback(
    Output('geolocate-info', 'children'),
    Input('geolocate-demo', 'geolocateInfo'),
    prevent_initial_call=True
)
def demo(geolocateInfo):

    return json.dumps(
        geolocateInfo,
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
