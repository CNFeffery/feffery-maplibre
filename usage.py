import json
import feffery_maplibre as fm
from dash import Dash, callback, html, Input, Output

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
            id='map-demo',
            mapStyle='https://api.maptiler.com/maps/basic-v2/style.json?key=pctRciYXNuENsTzDTtAS',
            initialViewState={
                'longitude': 106,
                'latitude': 29,
                'zoom': 3,
                'pitch': 45,
                'bearing': 45,
            },
            debounceWait=200,
            locale={
                'NavigationControl.ZoomIn': '放大地图',
                'NavigationControl.ZoomOut': '缩小地图',
                'NavigationControl.ResetBearing': '重置地图角度'
            },
            style={
                'width': '100vw',
                'height': 'calc(100vh - 300px)'
            },
            # enableDeckGL=True
        ),
        html.Button(
            'longitude=>0',
            id='set-longitude-0'
        ),
        html.Pre(id='test-props')
    ]
)


@app.callback(
    Output('test-props', 'children'),
    [
        Input('map-demo', 'longitudeDebounce'),
        Input('map-demo', 'latitudeDebounce'),
        Input('map-demo', 'zoomDebounce'),
        Input('map-demo', 'pitchDebounce'),
        Input('map-demo', 'bearingDebounce'),
        Input('map-demo', 'clickedLngLat'),
    ]
)
def show_test_props(longitudeDebounce,
                    latitudeDebounce,
                    zoomDebounce,
                    pitchDebounce,
                    bearingDebounce,
                    clickedLngLat):

    return json.dumps(
        dict(
            longitudeDebounce=longitudeDebounce,
            latitudeDebounce=latitudeDebounce,
            zoomDebounce=zoomDebounce,
            pitchDebounce=pitchDebounce,
            bearingDebounce=bearingDebounce,
            clickedLngLat=clickedLngLat
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    [Output('map-demo', 'longitude'),
     Output('map-demo', 'longitudeDebounce')],
    Input('set-longitude-0', 'n_clicks'),
    prevent_initial_call=True
)
def set_longitude_0(n_clicks):

    return 0, 0


if __name__ == '__main__':
    app.run_server(debug=True)
