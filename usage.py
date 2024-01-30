import dash
from dash import Dash, html
import feffery_maplibre as fm
from dash.dependencies import Input, Output

app = Dash(__name__)

colors = ['red', 'blue', 'yellow']

app.layout = html.Div(
    [
        fm.MapContainer(
            [
                # 热力图层测试
                fm.HeatmapLayer(
                    data='https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-bike-parking.json',
                    getPosition='COORDINATES',
                    radiusPixels=25
                ),

                # 图层排序操作
                fm.Fragment(
                    id='action-target'
                ),

                fm.SourceGroup(
                    [
                        fm.Source(
                            fm.Layer(
                                id=f'demo-layer{i+1}',
                                layerProps={
                                    'type': 'fill',
                                    'paint': {
                                        'fill-color': colors[i]
                                    }
                                }
                            ),
                            id=f'demo-source{i+1}',
                            sourceProps={
                                'type': 'geojson',
                                # 模拟生成面要素
                                'data': {
                                        'type': 'FeatureCollection',
                                        'features': [
                                            {
                                                'type': 'Feature',
                                                'geometry': {
                                                    'type': 'Polygon',
                                                    'coordinates': [
                                                        [
                                                            [-4+i*3, -2+i],
                                                            [-4+i*3, 2+i],
                                                            [0+i*3, 2+i],
                                                            [0+i*3, -2+i],
                                                            [-4+i*3, -2+i],
                                                        ]
                                                    ]
                                                }
                                            }
                                        ]
                                }
                            }
                        )
                        for i in range(3)
                    ]
                )
            ],
            initialViewState={
                'zoom': 5
            },
            style={
                'height': '100%'
            }
        ),

        html.Div(
            [
                html.Button(
                    '翻转图层顺序',
                    id='reverse-layers-order'
                )
            ],
            style={
                'background': 'white',
                'padding': '24px',
                'borderRadius': 6,
                'position': 'absolute',
                'zIndex': 9,
                'top': 12,
                'right': 12,
                'border': '1px solid #bfbfbf',
                'width': 300,
            }
        )
    ],
    style={
        'height': '100vh',
        'position': 'relative'
    }
)


@app.callback(
    Output('action-target', 'children'),
    Input('reverse-layers-order', 'n_clicks'),
    prevent_initial_call=True
)
def handle_layers_order_update(n_clicks):

    if dash.ctx.triggered_id == 'reverse-layers-order':
        return fm.SortLayers(
            orders=(
                [
                    'demo-layer3',
                    'demo-layer2',
                    'demo-layer1'
                ]
                if n_clicks % 2 else
                [
                    'demo-layer1',
                    'demo-layer2',
                    'demo-layer3'
                ]
            )
        )


if __name__ == '__main__':
    app.run_server(debug=True)
