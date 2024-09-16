import React from 'react'

import StudioButton from 'material/buttons/StudioButton'


const LandingPageRoutes = ['/']


class LandingPage extends React.Component {
    render() {
        return (
            <div className='landing-page-wrapper'>
                <div className='landing-page-container'>
                    <h1>Full Stack Dev</h1>
                    <h2>Tutorial Series</h2>

                    <StudioButton
                    text='JWT Protected Route'
                    href='/auth/protected-route'
                    variant='contained'
                    size='large'/>
                </div>
            </div>
        )
    }
}

LandingPage.routes = LandingPageRoutes


export default LandingPage
