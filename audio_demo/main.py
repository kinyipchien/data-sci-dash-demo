import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Hello Dasher', style={'color': 'purple'}),
    html.Audio(id='a1', src='/assets/t1.wav', controls=True, autoPlay=False),
    html.Label(id='l1', children='hello'),
    html.Button(id='submit', n_clicks=0, children='Submit'),
])

@app.callback([Output('a1', 'src'), Output('l1', 'children')],
              [Input('submit', 'n_clicks')])
def update_audio(n_clicks):
    print('clicks:', n_clicks)
    if n_clicks < 10:
        return '/assets/t2.wav', 'lol'
    return '/assets/t3.wav', 'default'


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5555)
