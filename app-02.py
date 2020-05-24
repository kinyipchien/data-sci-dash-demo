import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pickle

model = pickle.load(open("../flask-app-ds/models/model.p", "rb"))
cv = pickle.load(open("../flask-app-ds/models/cv.p", "rb"))
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Callback'),
    dcc.Input(id='my-input', value='initial value', type='text'),
    html.Div(id='my-output')
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return "{} was entered, also you have {} classes".format(input_value, model.classes_)


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5555, dev_tools_hot_reload=False)
