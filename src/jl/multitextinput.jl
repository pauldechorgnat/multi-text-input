# AUTO GENERATED FILE - DO NOT EDIT

export multitextinput

"""
    multitextinput(;kwargs...)

A MultiTextInput component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `label` (String; optional): A label that will be printed when this component is rendered.
- `placeholder` (String; optional)
- `value` (String; optional): The value displayed in the input.
- `values` (Array of Strings; optional): The values validated by the input.
"""
function multitextinput(; kwargs...)
        available_props = Symbol[:id, :label, :placeholder, :value, :values]
        wild_props = Symbol[]
        return Component("multitextinput", "MultiTextInput", "multi_text_input", available_props, wild_props; kwargs...)
end

