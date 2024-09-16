import React from 'react'
import PropTypes from 'prop-types'

import InputAdornment from '@mui/material/InputAdornment'
import TextField from '@mui/material/TextField'
import Tooltip from '@mui/material/Tooltip'
import VisibilityOffRoundedIcon from '@mui/icons-material/VisibilityOffRounded'
import VisibilityRoundedIcon from '@mui/icons-material/VisibilityRounded'


let StudioInputPropTypes = {
    autoComplete: PropTypes.string,
    autoFocus: PropTypes.bool,
    children: PropTypes.node,
    classes: PropTypes.object,
    className: PropTypes.string,
    color: PropTypes.oneOf(['primary', 'secondary', PropTypes.string]),
    components: PropTypes.elementType,
    defaultValue: PropTypes.any,
    disabled: PropTypes.bool,
    endAdornment: PropTypes.node,
    error: PropTypes.bool,
    fullWidth: PropTypes.bool,
    helperText: PropTypes.node,
    id: PropTypes.string,
    inputComponent: PropTypes.elementType,
    inputProps: PropTypes.object,
    inputRef: PropTypes.oneOfType([
        PropTypes.func,
        PropTypes.shape({ current: PropTypes.any }),
    ]),
    labelText: PropTypes.string,
    margin: PropTypes.oneOf(['dense', 'none']),
    maxRows: PropTypes.oneOf([PropTypes.number, PropTypes.string]),
    minRows: PropTypes.oneOf([PropTypes.number, PropTypes.string]),
    multiline: PropTypes.bool,
    name: PropTypes.string,
    onChange: PropTypes.func,
    placeholder: PropTypes.string,
    readOnly: PropTypes.bool,
    required: PropTypes.bool,
    rows: PropTypes.oneOf([PropTypes.number, PropTypes.string]),
    select: PropTypes.bool,
    size: PropTypes.oneOf(['medium', 'small', PropTypes.string]),
    tooltipTitle: PropTypes.node,
    type: PropTypes.string,
    value: PropTypes.any,
    variant: PropTypes.oneOf(['filled', 'outlined', 'standard']),
    tooltipPlacement: PropTypes.string,
    tooltipDelay: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
}

let StudioInputDefaultProps = {
    autoComplete: 'on',
    autoFocus: false,
    children: null,
    classes: null,
    className: 'studio-input',
    color: null,
    components: null,
    defaultValue: undefined,
    disabled: false,
    error: false,
    fullWidth: true,
    helperText: null,
    labelText: null,
    margin: 'dense',
    name: null,
    onChange: ()=>{},
    placeholder: null,
    readOnly: false,
    required: false,
    select: false,
    size: 'small',
    tooltipTitle: null,
    type: 'text',
    value: null,
    variant: 'outlined',
    tooltipPlacement: 'top',
    tooltipDelay: 750,
}


class StudioInput extends React.Component {
    constructor(props) {super(props)
        this.state = {
            showPassword: false,
            type: this.props.type,
        }
    }

    render() {
        return !this.props.disabled ? (
            this.renderInput()
        ) : this.renderTextRepresentation()
    }

    renderInput() {
        return (
            <Tooltip
            className='studio-tooltip'
            title={this.props.tooltipTitle}
            placement={this.props.tooltipPlacement}
            enterDelay={Number(this.props.tooltipDelay)}>
                {this.renderTextField()}
            </Tooltip>
        )
    }

    renderTextRepresentation() {
        let hidden = this.props.value === '' ? true : false

        return (
            <h5 style={hidden ? { display: 'none' } : null}>
                {this.props.value}
            </h5>
        )
    }

    renderTextField() {
        return (
            <TextField
            InputProps={this.inputProps()}

            autoComplete={this.props.autoComplete}
            autoFocus={this.props.autoFocus}
            children={this.props.children}
            className={this.props.className}
            classes={this.props.classes}
            color={this.props.color}
            components={this.props.components}
            defaultValue={this.props.defaultValue}
            error={this.props.error}
            fullWidth={this.props.fullWidth}
            helperText={this.props.helperText}
            inputProps={this.props.inputProps}
            label={this.props.labelText}
            margin={this.props.margin}
            name={this.props.name}
            onChange={this.props.onChange}
            placeholder={this.props.placeholder}
            readOnly={this.props.readOnly}
            required={this.props.required}
            select={this.props.select}
            size={this.props.size}
            type={this.state.type}  // state managed when needed
            value={this.props.value}
            variant={this.props.variant}/>
        )
    }

    inputProps() {
        return this.props.type === 'password' ? ({
            endAdornment:
            <InputAdornment className='toggle-password-visible' position='end'>
                {this.state.showPassword ? (
                    <VisibilityOffRoundedIcon
                    onClick={() => this.togglePasswordVisible()}/>
                ) : <VisibilityRoundedIcon
                    onClick={() => this.togglePasswordVisible()}/>}
            </InputAdornment>
        }) : null
    }

    togglePasswordVisible() {
        this.setState({showPassword: !this.state.showPassword})

        this.state.showPassword ? (
            this.setState({type: 'password'})
        ) : this.setState({type: 'text'})
    }
}


StudioInput.propTypes = StudioInputPropTypes
StudioInput.defaultProps = StudioInputDefaultProps


export default StudioInput
