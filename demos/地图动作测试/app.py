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

    ],
    style={
        'height': '100vh'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
