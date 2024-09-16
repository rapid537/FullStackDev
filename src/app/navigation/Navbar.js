import {Link} from 'react-router-dom'
import {HomeRounded, Menu} from '@mui/icons-material'

import StudioButton from 'material/buttons/StudioButton'
import StudioManager from 'rest/StudioManager'


class Navbar extends StudioManager {
    constructor(props) {super(props)
        this.state = {showModal: false}
    }

    render() {
        return (
            <div className='navbar'>
                {this.renderMenu()}
                {this.renderMenuModal()}
            </div>
        )
    }

    renderMenu() {
        return (
            <div
            className='navbar-menu'
            onClick={() => this.setState({
                showModal: !this.state.showModal,
            })}>
                <Menu/>
            </div>
        )
    }

    renderMenuModal() {
        return (
            this.state.showModal ? (
                <div className='navbar-modal'>
                    {this.renderAccountOptions()}
                </div>
            ) : null
        )
    }

    renderAccountOptions() {
        return (
            <div className='account-options-wrapper'>
                <h5>session</h5>

                <div
                className='account-options'
                onClick={() => this.setState({showModal: false})}>

                    {this.hasAccessToken ? (
                        this.renderOptions_isSession()
                    ) : (
                        this.renderOptions_isNotSession()
                    )}

                    {this.renderAccountOptionsIcons()}

                </div>
            </div>
        )
    }

    renderOptions_isSession() {
        return (
            <>
                <h6>end session</h6>
                <StudioButton
                text='Sign Out'
                variant='contained'
                size='small'
                onClick={() => this.signOut()}/>
            </>
        )
    }

    renderOptions_isNotSession() {
        return (
            <>
                <h6>sign in</h6>

                <StudioButton
                text='Sign In'
                href='/auth/sign-in'
                variant='contained'
                size='small'/>

                <h6>don't have an account?</h6>

                <StudioButton
                text='Sign Up'
                href='/auth/sign-up'
                variant='contained'
                size='small'/>
            </>
        )
    }

    renderAccountOptionsIcons() {
        return (
            <div className='account-options-icon-bar'>
                {this.renderHomeLink()}
            </div>
        )
    }

    renderHomeLink() {
        return (
            <Link to='/'>
                <HomeRounded className='studio-toolbar-settings-button'/>
            </Link>
        )
    }

    signOut() {
        this.REST.POST('sign_out')
        .then(() => sessionStorage.removeItem('context'))
    }
}


export default Navbar
