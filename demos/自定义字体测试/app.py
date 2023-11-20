if True:
    import sys
    sys.path.append('../..')

    import dash
    import random
    from dash import html
    import feffery_maplibre as fm

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                ),

                # 调用esri开放影像底图
                fm.Source(
                    [
                        fm.Layer(
                            id='img-layer',
                            layerProps={
                                'type': 'raster',
                                'source': 'img-source'
                            }
                        )
                    ],
                    id='img-source',
                    sourceProps={
                        'type': 'raster',
                        'tiles': [
                            'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        ],
                        'tileSize': 256
                    }
                ),

                # 点要素示例
                fm.Source(
                    [
                        fm.Layer(
                            id='points-layer',
                            layerProps={
                                'type': 'symbol',
                                'layout': {
                                    'text-field': '{name}',
                                    'text-size': 20,
                                    'text-font': [
                                        'STXinwei Regular'
                                    ],
                                    'text-allow-overlap': True
                                },
                                'paint': {
                                    'text-color': 'white',
                                    'text-halo-color': '#000000',
                                    'text-halo-width': 3
                                }
                            }
                        )
                    ],
                    id='points-source',
                    sourceProps={
                        'type': 'geojson',
                        'data': {
                            'type': 'FeatureCollection',
                            'features': [
                                {
                                    'type': 'Feature',
                                    'geometry': {
                                        'type': 'Point',
                                        'coordinates': [random.uniform(-45, 45), random.uniform(-45, 45)]
                                    },
                                    'properties': {
                                        'name': f'测试{i}'
                                    }
                                }
                                for i in range(100)
                            ]
                        }
                    }
                )
            ],
            style={
                'height': '100%'
            },
            mapStyle={
                'version': 8,
                'sources': {},
                'layers': [],
                'glyphs': 'http://127.0.0.1:3000/font/{fontstack}/{range}'
            },
            initialViewState={
                'zoom': 2
            }
        )
    ],
    style={
        'height': '100vh'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
