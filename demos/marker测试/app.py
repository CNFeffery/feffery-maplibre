if True:
    import sys
    sys.path.append('../..')

    import dash
    from dash import html
    import feffery_maplibre as fm
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fm.MapContainer(
            [
                # 基础底图控制
                fm.SourceGroup(
                    [
                        fm.Source(
                            [
                                fm.Layer(
                                    id='digits-map-img-layer',
                                    layerProps={
                                        'type': 'raster',
                                        'source': 'digits-map-img-source'
                                    }
                                )
                            ],
                            id='digits-map-img-source',
                            sourceProps={
                                'type': 'raster',
                                'tiles': [
                                    'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                ],
                                'tileSize': 256
                            }
                        ),
                        fm.Source(
                            [
                                fm.Layer(
                                    id='digits-map-cia-layer',
                                    layerProps={
                                        'type': 'raster',
                                        'source': 'digits-map-cia-source'
                                    }
                                )
                            ],
                            id='digits-map-cia-source',
                            sourceProps={
                                'type': 'raster',
                                'tiles': [
                                    'http://t4.tianditu.gov.cn/cia_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cia&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&tk=862c8d3fc40aa77c70adca25ae4feef5',
                                ],
                                'tileSize': 256
                            }
                        )
                    ]
                ),
                # fm.Marker(
                #     # html.Span(
                #     #     '测试',
                #     #     style={
                #     #         'fontSize': 50,
                #     #         'color': 'white'
                #     #     }
                #     # ),
                #     latitude=0,
                #     longitude=0,
                #     color='#ff6b6b',
                #     draggable=True
                # ),
                # fm.Popup(
                #     '测试内容',
                #     latitude=0,
                #     longitude=0
                # )
            ],
            initialViewState={
                'longitude': 0,
                'latitude': 0,
                'zoom': 3,
                'pitch': 0,
                'bearing': 0,
            },
            # mapStyle='https://api.maptiler.com/maps/hybrid/style.json?key=pctRciYXNuENsTzDTtAS',
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
    app.run(debug=True, port=8002)
