import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Hello Dasher', style={'color': 'purple'}),
    html.Img(src=app.get_asset_url('image.jpg'), style={'width': '250px'}),
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5555)
