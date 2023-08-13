# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MultiTextInput(Component):
    """A MultiTextInput component.
    ExampleComponent is an example component.
    It takes a property, `label`, and
    displays it.
    It renders an input with the property `value`
    which is editable by the user.

    Keyword arguments:

    - id (string; optional):
        The ID used to identify this component in Dash callbacks.

    - label (string; optional):
        A label that will be printed when this component is rendered.

    - placeholder (string; default "Press enter to add new text")

    - value (string; optional):
        The value displayed in the input.

    - values (list of strings; optional):
        The values validated by the input."""

    _children_props = ["values"]
    _base_nodes = ["children"]
    _namespace = "multi_text_input"
    _type = "MultiTextInput"

    @_explicitize_args
    def __init__(
        self,
        id=Component.UNDEFINED,
        label=Component.UNDEFINED,
        value=Component.UNDEFINED,
        values=Component.UNDEFINED,
        placeholder=Component.UNDEFINED,
        **kwargs
    ):
        self._prop_names = ["id", "label", "placeholder", "value", "values"]
        self._valid_wildcard_attributes = []
        self.available_properties = ["id", "label", "placeholder", "value", "values"]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop("_explicit_args")
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MultiTextInput, self).__init__(**args)
