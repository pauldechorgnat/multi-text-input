import multi_text_input
from dash import Dash, html, Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    multi_text_input.MultiTextInput(
        id='input',
        # value='my-value',
        placeholder="Press enter key to validate",
        label='my-label',
        values=["hello", "bonjour", "hola"]
    ),
    html.Div(id='output')
])

# print(multi_text_input.MultiTextInput.values)


@app.callback(
    Output('output', 'children'),
    Input('input', 'values'),
    
)
def display_output(values):
    print(values)
    return 'You have entered "{}"'.format(values)


if __name__ == '__main__':
    app.run_server(debug=True)
