if True:
    import sys
    sys.path.append('../..')

    import dash
    from dash import html
    import feffery_maplibre as fm

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fm.MapContainer(
            [
                fm.TerrainLayer(
                    id='terrain-demo',
                    elevationData='https://demotiles.maplibre.org/terrain-tiles/{z}/{x}/{y}.png',
                    texture='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    # bounds=[
                    #     -180,
                    #     -85.05112877980659,
                    #     180,
                    #     85.0511287798066
                    # ],
                    # wireframe=True
                )
            ],
            initialViewState={
                'longitude': 11.39085,
                'latitude': 47.27574,
                'zoom': 12,
                'pitch': 52,
                'bearing': 0
            },
            maxZoom=18,
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
