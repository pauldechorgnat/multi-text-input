# MultiTextInput

`multi-text-input` is a Dash component library. Its only component is called `MultiTextInput` and allows you to easily create custom lists of strings with a simple interface and delete some elements from that list. The Github repository is available [here](https://github.com/pauldechorgnat/multi-text-input/).

![Demo of multi-text-input](https://github.com/pauldechorgnat/multi-text-input/demo-multi-text-input-dash.gif)

## Usage

This component is available as as [Python library](https://pypi.org/project/multi-text-input/0.0.1/).

You can install it by running: 

```sh
pip install multi-text-input
```

The following shows a simple application of this 

```python
from dash import Dash, dcc, html, Input, Output, State
from multi_text_input import MultiTextInput

app = Dash(__name__)

app.layout = html.Div(
    [
        MultiTextInput(id="input"),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("output", "children"),
    Input("input", "values"),
)
def update_output(input1):
    print(input1)
    return str(input1)

if __name__ == "__main__":
    app.run(debug=True)
```

## Properties

`MultiTextInput` constructor can take: 

- `placeholder`: to change the placeholder value
- `value`: to change the starting value inside the text input
- `values`: to change the validated values (the buttons)
- `id` and `label`

Buttons are from the `multi-text-input-item` class if you want to change their design.

For callbacks, you can access the `value` and `values` properties of `MultiTextInput`:

- `value` is the actual value in the text input
- `values` is all the values of the list
