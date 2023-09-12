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
                ),

                fm.GeoJsonLayer(
                    id='demo-geo-json-layer-line',
                    data='https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart.geo.json',
                    extruded=True,
                    filled=True,
                    getElevation=30,
                    getFillColor=[160, 160, 180, 200],
                    getLineColor={
                        'func': '''f => {
    const hex = f.properties.color;
    // convert to RGB
    return hex ? hex.match(/[0-9a-f]{2}/g).map(x => parseInt(x, 16)) : [0, 0, 0];
  }'''
                    },
                    getLineWidth=20,
                    getPointRadius=4,
                    lineWidthMinPixels=2,
                    pointRadiusUnits='pixels',
                    stroked=False,
                    pickable=True,
                    tooltipRenderer='({object}) => object && (object.properties.name || object.properties.station)',
                    lineWidthUnits='meters',
                ),

                fm.GeoJsonLayer(
                    id='demo-geo-json-layer-polygon',
                    data='https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json',
                    opacity=0.8,
                    stroked=False,
                    filled=True,
                    extruded=True,
                    wireframe=True,
                    getElevation={
                        'func': 'f => Math.sqrt(f.properties.valuePerSqm) * 10'
                    },
                    getLineColor=[255, 255, 255],
                    getFillColor={
                        'func': '''(item) => {
                            if ( item.properties.valuePerSqm >= 8000 ) {
                                return [255, 77, 79];
                            }
                            return [105, 192, 255];
                        }'''
                    },
                    getLineWidth=2,
                    pickable=True,
                    tooltipRenderer='''({object}) => {
  return (
    object && {
      html: `\
  <div><b>Average Property Value</b></div>
  <div>${object.properties.valuePerParcel} / parcel</div>
  <div>${object.properties.valuePerSqm} / m<sup>2</sup></div>
  <div><b>Growth</b></div>
  <div>${Math.round(object.properties.growth * 100)}%</div>
  `
    }
  );
}'''
                )
            ],
            initialViewState={
                'latitude': 49.254,
                'longitude': -123.13,
                'zoom': 11,
                'pitch': 45,
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
