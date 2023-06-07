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
                fm.ScaleControl(),

                fm.Source(
                    [
                        fm.Layer(
                            id='mapbox-demo-layer-landuse',
                            layerProps={
                                'source-layer': 'landuse',
                                'type': 'fill',
                                'paint':  {
                                    'fill-color': 'green',
                                    'fill-outline-color': 'green'
                                }
                            },
                            hoverCursor='pointer'
                        ),
                        fm.Layer(
                            id='mapbox-demo-country_label',
                            layerProps={
                                'source-layer': 'country_label',
                                'type': 'circle'
                            },
                            hoverCursor='pointer'
                        )
                    ],
                    id='mapbox-demo-source',
                    sourceProps={
                        'tiles':  [
                            'https://b.tiles.mapbox.com/v4/mapbox.mapbox-streets-v6/{z}/{x}/{y}.vector.pbf?sku=101SPH62Z4zzs&access_token=pk.eyJ1IjoiZmVmZmVyeXB6eSIsImEiOiJjanhyY2QyenUwN2VzM2x0NWh6MGVzOWFqIn0.Z2HEVP_nJ8Smx_IWxkdRqg'
                        ],
                        'type': 'vector'
                    }
                ),

                # fm.Source(
                #     [
                #         fm.Layer(
                #             id='demo-layer',
                #             layerProps={
                #                 'source-layer': 'dt860',
                #                 'type': 'fill',
                #                 'paint': {
                #                     'fill-color': '#81ecec',
                #                     'fill-opacity': 0.4,
                #                     'fill-outline-color': 'black'
                #                 }
                #             },
                #             hoverCursor='pointer'
                #         )
                #     ],
                #     id='demo-source',
                #     sourceProps={
                #         'tiles': [
                #             'http://10.10.0.26:9101/mapserver/tms/1.0.0/cu:dt860@EPSG:900913@pbf/{z}/{x}/{y}.pbf'
                #         ],
                #         'type': 'vector',
                #         'scheme': 'tms'
                #     }
                # )
            ],
            id='map-demo',
            mapStyle='https://api.maptiler.com/maps/basic-v2/style.json?key=pctRciYXNuENsTzDTtAS',
            initialViewState={
                'longitude': 106,
                'latitude': 29,
                'zoom': 7,
                'pitch': 45,
                'bearing': 45,
            },
            clickListenLayerIds=[
                'mapbox-demo-layer-landuse',
                'mapbox-demo-country_label'
            ],
            clickListenBoxSize=100,
            debounceWait=200,
            locale={
                'NavigationControl.ZoomIn': '放大地图',
                'NavigationControl.ZoomOut': '缩小地图',
                'NavigationControl.ResetBearing': '重置地图角度'
            },
            style={
                'width': '100vw',
                'height': 'calc(100vh - 300px)'
            }
            # enableDeckGL=True
        ),
        html.Div(
            [
                html.Button(
                    'longitude=>0',
                    id='set-longitude-0'
                )
            ]
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
        Input('map-demo', 'clickListenLayerFeatures')
    ]
)
def show_test_props(longitudeDebounce,
                    latitudeDebounce,
                    zoomDebounce,
                    pitchDebounce,
                    bearingDebounce,
                    clickedLngLat,
                    clickListenLayerFeatures):

    return json.dumps(
        dict(
            longitudeDebounce=longitudeDebounce,
            latitudeDebounce=latitudeDebounce,
            zoomDebounce=zoomDebounce,
            pitchDebounce=pitchDebounce,
            bearingDebounce=bearingDebounce,
            clickedLngLat=clickedLngLat,
            clickListenLayerFeatures=clickListenLayerFeatures
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
