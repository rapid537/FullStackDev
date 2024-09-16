import React from 'react'
import PropTypes from 'prop-types'

let StudioTitleBarPropTypes = {
    title: PropTypes.string.isRequired,
    variant: PropTypes.oneOf(['dark-theme', 'light-theme']),
}

let StudioTitleBarDefaultProps = {
    variant: 'dark-theme',
}


class StudioTitleBar extends React.Component {
    render() {
        return (
            <p className={`title-bar ${this.props.variant}`}>
                {this.props.title}
            </p>
        )
    }
}


StudioTitleBar.propTypes = StudioTitleBarPropTypes
StudioTitleBar.defaultProps = StudioTitleBarDefaultProps

export default StudioTitleBar
