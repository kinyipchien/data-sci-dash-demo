import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import subprocess

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Hello Callback'),
    dcc.Input(id='my-input1', value='5', type='number'),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(id='my-dd1',
                 options=[
                     {'label': 'New York City', 'value': 'NYC'},
                     {'label': u'Montréal', 'value': 'MTL'},
                     {'label': 'San Francisco', 'value': 'SF'}
                 ],
                 value=['MTL'],
                 multi=True
                 ),
    html.Div(id='my-output1', style={'color': 'green'})
])


@app.callback(
    Output('my-output1', 'children'),
    [Input('my-dd1', 'value')]
)
def update(input_value):
    print('server, type:', type(input_value), 'val:', input_value)

    cmd = ['python', 'receiver.py'] + input_value
    print('command:', cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    outputs = []
    for line in p.stdout.readlines():
        print('line:', line)
        outputs.append(line)
    print('call complete', outputs)
    roll = int(outputs[-2])

    # pd.load_csv(outputs[-1])
    print('rooll', roll)

    return "{} was entered and received {} from my other process".format(input_value, roll)


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5555, dev_tools_hot_reload=False)
