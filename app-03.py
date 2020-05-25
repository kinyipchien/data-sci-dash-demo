import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State
import pickle

model = pickle.load(open("../flask-app-ds/models/model.p", "rb"))
cv = pickle.load(open("../flask-app-ds/models/cv.p", "rb"))
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# show these controls
# pip install dash_daq
# https://dash.plotly.com/dash-daq

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #

app.layout = html.Div([
    html.H1('Game Review Sentiment'),
    dcc.Input(id='input-review', type='text', value='enter review here'),
    html.Button(id='submit-review', n_clicks=0, children='Submit'),
    daq.LEDDisplay(
        id='is_positive',
        value="0",
        label="P(postive review | text)",
        color="#ff33cc",
        style={'display': 'flex'}
    ),
    dcc.Graph(
        id='bar_chart',
        style={'border': '1px dashed #ff33cc', 'width': '350px', 'marginTop': '20px', 'height': '300px'}
    )
])

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


@app.callback([Output('is_positive', 'value'),
               Output('bar_chart', 'figure')],
              [Input('submit-review', 'n_clicks')],
              [State('input-review', 'value')])
def update_review(n_clicks, review):
    vector = cv.transform([review])
    prediction = model.predict_proba(vector)
    c0, c1 = prediction[0]

    figure = {
        'data': [{
            'x': ['P(-|text)', 'P(+|text)'],
            'y': [c0, c1],
            'type': 'bar',
            'name': 'Sentiment'
        }],
        'layout': {'title': 'Sentiment Analysis', 'yaxis': {'range': [0, 1]}}
    }

    return c1.round(3), figure

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5555, dev_tools_hot_reload=False)
