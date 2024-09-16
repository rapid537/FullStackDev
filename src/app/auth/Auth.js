import React from 'react'
import {Route} from 'react-router-dom'

import ConfirmCodeForm from 'app/auth/components/ConfirmCodeForm'
import ProtectedRoute from 'app/auth/components/ProtectedRoute'
import SignInForm from 'app/auth/components/SignInForm'
import SignUpForm from 'app/auth/components/SignUpForm'


const AuthRoutes = ['/auth/:route',]


class Auth extends React.Component {
    render() {
        return (
            <div className='auth-container'>
                <Route path='/auth/sign-in' exact component={SignInForm}/>
                <Route path='/auth/sign-up' exact component={SignUpForm}/>
                <Route path='/auth/confirm-code' exact component={ConfirmCodeForm}/>
                <Route path='/auth/protected-route' exact component={ProtectedRoute}/>
            </div>
        )
    }
}

Auth.routes = AuthRoutes


export default Auth
