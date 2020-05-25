import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pickle

model = pickle.load(open("../flask-app-ds/models/model.p", "rb"))
cv = pickle.load(open("../flask-app-ds/models/cv.p", "rb"))
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #

app.layout = html.Div(children=[
    html.H1(children='Hello Callback'),
    dcc.Input(id='my-input1', value='initial value', type='text'),
    dcc.Input(id='my-input2', value='3', type='number'),
    dcc.Input(id='my-input3', value='5', type='number'),
    html.Div(id='my-output1'),
    html.Div(id='my-output2'),
    html.Div(id='my-output3'),
    html.Div(id='my-output4')
])

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


@app.callback(
    # basic callback
    # input HAS to be LIST
    # output ONLY list, if it has multiple values
    Output(component_id='my-output1', component_property='children'),
    [Input(component_id='my-input1', component_property='value')]
)
def update_output_div1(input_value):
    return "{} was entered".format(input_value)

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


@app.callback(
    # calculation on input
    Output(component_id='my-output2', component_property='children'),
    [Input(component_id='my-input2', component_property='value')]
)
def update_output_div2(input_value):
    print('input:', input_value, 'type:', type(input_value))
    val = float(input_value)
    return "the square of {} is {}".format(val, val ** 2)

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


@app.callback(
    # calculation with multiple inputs
    [
        Output(component_id='my-output3', component_property='children'),
        Output(component_id='my-output4', component_property='children')
    ],
    [
        Input(component_id='my-input2', component_property='value'),
        Input(component_id='my-input3', component_property='value')
    ]
)
def update_output_div3(in1, in2):
    val1 = float(in1)
    val2 = float(in2)
    s1 = "the product of {} and {} is {}".format(val1, val2, val1 * val2)
    s2 = "the sum of {} and {} is {}".format(val1, val2, val1 + val2)
    return s1, s2


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5555, dev_tools_hot_reload=False)
