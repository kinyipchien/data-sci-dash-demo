import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown = '''
# header

## second header

- 1
- 2
- 3
'''

mainstyle = {'color': 'green', 'width': '500px'}

app.layout = html.Div(style=mainstyle, children=[
    html.H1(children='Hello Dasher', style={'color': 'purple'}),

    html.Img(src="https://www.laarchaeology.org/wp-content/uploads/2017/11/science.jpg", style={'width': '250px'}),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Div([
        dcc.Markdown(markdown)
    ]),

    html.Ul(children=[
        html.Li('first', style={'border': '1px dashed red'}),
        html.Li('second', style={'backgroundColor': 'yellow', 'padding': '50px'}),
        html.Li('third', style={'color': 'blue'})
    ]),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 9, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization - Super Cool'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5555)
