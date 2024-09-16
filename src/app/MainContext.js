import {getGlobal, setGlobal} from 'reactn'


export function initContext() {
    return JSON.parse(sessionStorage.getItem('context')) || {
        app_1: {  // customize object/s to your preference
            app_data: 0,
            app_items: [],
            app_objects: {},
        },
        user: {
            userName: 'guest',
            userMail: undefined,
        },
    }
}

export function stateful(obj) {
    setGlobal(
        Object.assign(getGlobal(), obj)
    )

    sessionStorage.setItem(
        'context',
        JSON.stringify(getGlobal()),
    )
}
