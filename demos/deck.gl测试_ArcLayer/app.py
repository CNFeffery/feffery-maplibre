if True:
    import sys
    sys.path.append('../..')

    import dash
    from dash import html
    import feffery_maplibre as fm
    from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

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

                fm.ArcLayer(
                    id='demo-arc-layer',
                    data='https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart-segments.json',
                    getWidth=12,
                    getHeight=3,
                    getSourcePosition='from.coordinates',
                    getTargetPosition='to.coordinates',
                    getSourceColor={
                        'func': 'd => [Math.sqrt(d.inbound), 140, 0]'
                    },
                    getTargetColor={
                        'func': 'd => [Math.sqrt(d.outbound), 140, 0]'
                    },
                    pickable=True,
                    highlightColor=[245, 34, 45],
                    autoHighlight=True,
                    tooltipRenderer='''({ object }) => {
                        if ( object ) {
                            return object && `${object.from.coordinates} -> ${object.to.coordinates}`;
                        }
                    }'''
                )
            ],
            initialViewState={
                'longitude': -122.4,
                'latitude': 37.74,
                'zoom': 11,
                'pitch': 30,
                'bearing': 0
            },
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
    app.run(debug=True, port=8050)
