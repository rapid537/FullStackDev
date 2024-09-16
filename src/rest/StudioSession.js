import React, {getGlobal, setGlobal} from 'reactn'

import {initContext, stateful} from 'app/MainContext'
import {hasAccessToken} from 'rest/Session'


class StudioSession extends React.Component {
    constructor(props) {super(props)
        setGlobal(initContext())
        this.SESSION = getGlobal()
        this.hasAccessToken = hasAccessToken()
    }

    stateful(obj) {
        stateful(obj)
    }
}


export default StudioSession
