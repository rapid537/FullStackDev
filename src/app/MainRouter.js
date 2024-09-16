import {BrowserRouter as Router, Switch} from 'react-router-dom'
import {Route} from 'react-router-dom'

import Auth from 'app/auth/Auth'
import LandingPage from 'app/landing/LandingPage'
import Navbar from 'app/navigation/Navbar'
import {toaster} from 'util/toast/Toast'


function registerRoutes() {
    return (
        <>
            <Route path={Auth.routes} exact component={Auth}/>
            <Route path={LandingPage.routes} exact component={LandingPage}/>
        </>
    )
}


function renderApp() {
    return (
        <div className='app-container'>
            <Navbar/>
            <Switch>
                {registerRoutes()}
            </Switch>
            {toaster()}
        </div>
    )
}


function MainRouter() {
    return (
        <Router>
            <div className='app-wrapper'>
                {renderApp()}
            </div>
        </Router>
    )
}


export default MainRouter
