import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */


export default class MultiTextInput extends Component {
    constructor(id, label, value, values, placeholder) {
        super();
        this.state = {
            values: values,
            value: value,
        }

    }
    render() {
        const {id, label, setProps, value, values, placeholder} = this.props;

        return (
            <div id={id}>
                {label}&nbsp;
                <input
                    value={value}
                    placeholder={placeholder}
                    onChange={
                        /*
                         * Send the new value to the parent component.
                         * setProps is a prop that is automatically supplied
                         * by dash's front-end ("dash-renderer").
                         * In a Dash app, this will update the component's
                         * props and send the data back to the Python Dash
                         * app server if a callback uses the modified prop as
                         * Input or State.
                         */
                        // e => {console.log(e.target.value)}
                        e => {
                            setProps({ value: e.target.value })
                            // console.log(e.target.value)
                            
                        }
                    }
                    onKeyDown={
                        e => {
                            if ((e.type === "keydown") & (e.keyCode == 13)) {
                                const newState = this.state;
                                values.push(e.target.value);
                                setProps({values: values})
                                setProps({ value: "" });
                                this.setState(newState);

                            }
                        }
                    }
                />
                <div>
                    {
                            values.map(
                                (item, index) => 
                                <button 
                                className="multi-text-input-item"
                                key={index}
                                style={{'marginRight': '.5em', 'marginTop': '.5em'}}
                                onClick={
                                    e => {
                                        const newState = this.state;
                                        values.splice(index, 1);
                                        console.log(values);
                                        setProps({values: values})
                                        this.setState(newState);

                                    }
                                }
                                >
                                    {item}
                                </button>
                                    
                            
                        )
                    }
                </div>
                
            </div>
        );
    }
}

MultiTextInput.defaultProps = {
    values: [],
    placeholder: "Press enter to add new text"
};

MultiTextInput.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string,

    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,
    /**
     * The values validated by the input.
     */
    values: PropTypes.arrayOf(PropTypes.string),

    placeholder: PropTypes.string,
    /**
     * Placeholder for the input
     */

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
