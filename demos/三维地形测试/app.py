if True:
    import sys
    sys.path.append('../..')

    import dash
    import json
    from dash import html
    import feffery_maplibre as fm

app = dash.Dash(__name__)


app.layout = html.Div(
    [
        fm.MapContainer(
            [
                fm.NavigationControl(
                    showCompass=True,
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
                            # 'https://a.tile.openstreetmap.org/{z}/{x}/{y}.png'
                        ],
                        'tileSize': 256
                    }
                ),
                fm.Source(
                    id='tile-test-source',
                    sourceProps={
                        'type': 'raster-dem',
                        'url': 'https://demotiles.maplibre.org/terrain-tiles/tiles.json',
                        'tileSize': 256
                    }
                )
            ],
            initialViewState={
                "longitude": 11.39085,
                "latitude": 47.27574,
                "zoom": 13.267,
                "pitch": 52,
                "bearing": 0
            },
            style={
                'height': '100%'
            },
            terrain={
                'source': 'tile-test-source',
                'exaggeration': 1
            },
            maxZoom=18,
            maxPitch=85,
            debug=True
        )
    ],
    style={
        'width': '800px',
        'height': '600px',
    }
)


if __name__ == '__main__':
    app.run(debug=True)
