if True:
    import sys
    sys.path.append('../..')

    import dash
    import uuid
    import random
    from dash import html
    import feffery_maplibre as fm
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

layer_props = {
    'mapbox-demo-layer-landuse': dict(
        id='mapbox-demo-layer-landuse',
        layerProps={
            'source-layer': 'landuse',
            'type': 'fill',
            'paint':  {
                'fill-color': 'green',
                'fill-opacity': 0.4,
                'fill-outline-color': 'green'
            }
        },
        hoverCursor='pointer'
    ),
    'mapbox-demo-country_label': dict(
        id='mapbox-demo-country_label',
        layerProps={
            'source-layer': 'country_label',
            'type': 'circle'
        },
        hoverCursor='pointer'
    ),
    'mapbox-demo-admin': dict(
        id='mapbox-demo-admin',
        layerProps={
            'source-layer': 'admin',
            'type': 'fill',
            'paint': {
                'fill-outline-color': '#faa2c1',
                'fill-opacity': 0
            }
        },
        hoverCursor='pointer'
    ),
    'mapbox-demo-water': dict(
        id='mapbox-demo-water',
        layerProps={
            'source-layer': 'water',
            'type': 'fill',
            'paint': {
                'fill-color': '#c5f6fa'
            }
        },
        hoverCursor='pointer'
    ),
    'mapbox-demo-road': dict(
        id='mapbox-demo-road',
        layerProps={
            'source-layer': 'road',
            'type': 'line',
            'paint': {
                'line-color': '#fab005'
            }
        },
        hoverCursor='pointer'
    )
}

app.layout = html.Div(
    [
        html.Div(
            [
                fuc.FefferySortableList(
                    id='layer-order',
                    items=[
                        {
                            'key': layer,
                            'content': layer,
                            'style': {
                                'padding': '10px',
                                'borderBottom': '1px solid #dee2e6'
                            }
                        }
                        for layer in [
                            'mapbox-demo-layer-landuse',
                            'mapbox-demo-country_label',
                            'mapbox-demo-admin',
                            'mapbox-demo-water',
                            'mapbox-demo-road'
                        ]
                    ]
                )
            ],
            style={
                'flex': 'none',
                'width': 400
            }
        ),

        html.Div(
            [
                fm.MapContainer(
                    [
                        fm.NavigationControl(
                            visualizePitch=True
                        ),
                        fm.ScaleControl(),

                        fm.Source(
                            id='mapbox-demo-source',
                            sourceProps={
                                'tiles':  [
                                    'https://b.tiles.mapbox.com/v4/mapbox.mapbox-streets-v6/{z}/{x}/{y}.vector.pbf?sku=101SPH62Z4zzs&access_token=pk.eyJ1IjoiZmVmZmVyeXB6eSIsImEiOiJjanhyY2QyenUwN2VzM2x0NWh6MGVzOWFqIn0.Z2HEVP_nJ8Smx_IWxkdRqg'
                                ],
                                'type': 'vector'
                            }
                        )
                    ],
                    initialViewState={
                        'longitude': 106,
                        'latitude': 29,
                        'zoom': 7,
                        'pitch': 45,
                        'bearing': 45,
                    },
                    style={
                        'width': '100%',
                        'height': '100vh'
                    }
                )
            ],
            style={
                'flex': 'auto'
            }
        )
    ],
    style={
        'height': '100vh',
        'display': 'flex'
    }
)


@app.callback(
    Output('mapbox-demo-source', 'children'),
    Input('layer-order', 'currentOrder')
)
def update_source_layers(currentOrder):

    return [
        fm.Layer(
            **layer_props[layer],
            key=str(uuid.uuid4())
        )
        for layer in currentOrder[::-1]
    ]


if __name__ == '__main__':
    app.run(debug=True, port=8001)
