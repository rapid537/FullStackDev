import React from 'react'
import PropTypes from 'prop-types'

import Button from '@mui/material/Button'
import {Link} from 'react-router-dom'
import Tooltip from '@mui/material/Tooltip'


let StudioButtonPropTypes = {
    children: PropTypes.node,
    classes: PropTypes.object,
    color: PropTypes.oneOf(
        ['inherit', 'primary', 'secondary', 'success', 'error', 'info', 'warning', PropTypes.string]
    ),
    component: PropTypes.elementType,
    disabled: PropTypes.bool,
    disableElevation: PropTypes.bool,
    disableFocusRipple: PropTypes.bool,
    disableRipple: PropTypes.bool,
    endIcon: PropTypes.node,
    fullWidth: PropTypes.bool,
    href: PropTypes.string,
    size: PropTypes.oneOf(['large', 'medium', 'small', PropTypes.string]),
    startIcon: PropTypes.node,
    sx: PropTypes.object,
    variant: PropTypes.oneOf(['contained', 'outlined', 'text', PropTypes.string]),
    className: PropTypes.string,
    text: PropTypes.string,
    type: PropTypes.oneOf(['button', 'reset', 'submit']),
    onClick: PropTypes.func,
    onMouseEnter: PropTypes.func,
    onMouseLeave: PropTypes.func,
    onMouseDown: PropTypes.func,
    onMouseUp: PropTypes.func,
    tooltipTitle: PropTypes.string,
    tooltipPlacement: PropTypes.string,
    tooltipDelay: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
}

let StudioButtonDefaultProps = {
    children: null,
    classes: null,
    color: 'info',
    component: null,
    disabled: false,
    disableElevation: false,
    disableFocusRipple: false,
    disableRipple: false,
    endIcon: null,
    fullWidth: false,
    href: null,
    size: 'small',
    startIcon: null,
    sx: null,
    variant: 'outlined',
    className: 'studio-button',
    text: 'Studio Button',
    tooltipTitle: null,
    tooltipPlacement: 'top',
    tooltipDelay: 750,
    type: 'button',
    onClick: () => void (0),
    onMouseEnter: () => void (0),
    onMouseLeave: () => void (0),
    onMouseDown: () => void (0),
    onMouseUp: () => void (0),
}


class StudioButton extends React.Component {
    constructor(props) {super(props)
        this.state = {}
    }

    render() {
        return this.renderButtonWithTooltip()
    }

    renderButtonWithTooltip() {
        return (
            <Tooltip
            className='studio-tooltip'
            title={this.props.tooltipTitle}
            placement={this.props.tooltipPlacement}
            enterDelay={Number(this.props.tooltipDelay)}>
                {this.renderButton()}
            </Tooltip>
        )
    }

    renderButton() {
        let className = this.props.color || 'primary'

        return (
            <Button
            children={this.props.children}
            classes={this.props.classes}
            color={this.props.color}
            component={this.makeComponent()}
            disabled={this.props.disabled}
            disableElevation={this.props.disableElevation}
            disableFocusRipple={this.props.disableFocusRipple}
            disableRipple={this.props.disableRipple}
            endIcon={this.props.endIcon}
            fullWidth={this.props.fullWidth}
            href={this.props.href}
            size={this.props.size}
            sx={this.props.sx}
            startIcon={this.props.startIcon}
            variant={this.props.variant}
            className={`studio-button ${className} ${this.props.className}`}
            text={this.props.text}
            type={this.props.type}
            onClick={this.props.onClick}
            onMouseEnter={this.props.onMouseEnter}
            onMouseLeave={this.props.onMouseLeave}
            onMouseDown={this.props.onMouseDown}
            onMouseUp={this.props.onMouseUp}>
                {this.props.text}
            </Button>
        )
    }

    makeComponent() {
        return this.props.href ? (
            React.Component(<Link to={this.props.href || null} />)
        ) : null
    }
}


StudioButton.propTypes = StudioButtonPropTypes
StudioButton.defaultProps = StudioButtonDefaultProps


export default StudioButton
