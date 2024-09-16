import axios from 'axios'
import Cookies from 'js-cookie'

import flash from 'util/flash/Flash'
import {toastify} from 'util/toast/Toast'


export const BASE_URL =
    window.Cypress || process.env.REACT_APP_USE_TEST_API
    ? 'http://code.dev.com:5001/api'
    : process.env.NODE_ENV === 'development'
    ? 'http://code.dev.com:5000/api'
    : process.env.NODE_ENV === 'production'
    && 'https://your-domain-example.net/api'


class REST {
    requestURL = route => `${BASE_URL}/${route}`

    defaultHeaders = () => ({
        'Access-Control-Allow-Credentials': true,
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
        'Access-Control-Allow-Headers': [
            'Content-Type',
            'Set-Cookie',
            'X-CSRF-TOKEN',
            'Accept',
            'Authorization',
            'Origin',
        ],
        'Access-Control-Allow-Origin': [BASE_URL],
        'Content-type': 'application/json; charset=utf-8',
        'X-CSRF-TOKEN': Cookies.get('csrf_access_token'),
    })

    async GET(route, payload=null, url=null, headers=null) {
        try {
            return await axios({
                method: 'get',
                url: url || this.requestURL(route),
                params: payload,
                withCredentials: true,
                headers: headers || this.defaultHeaders(),
            })
            .then(response => this._handleFlaskResponse(response, payload))
        }
        catch (error) {
            this._handleFlaskResponse(error.response)
        }
    }

    async POST(route, payload=null, url=null, headers=null) {
        try {
            return await axios({
                method: 'post',
                url: url || this.requestURL(route),
                data: payload,
                withCredentials: true,
                headers: headers || this.defaultHeaders(),
            })
            .then(response => this._handleFlaskResponse(response, payload))
        }
        catch (error) {
            this._handleFlaskResponse(error.response)
        }
    }

    async DELETE(route, payload=null, url=null, headers=null) {
        try {
            return await axios({
                method: 'delete',
                url: url || this.requestURL(route),
                data: payload,
                withCredentials: true,
                headers: headers || this.defaultHeaders(),
            })
            .then(response => this._handleFlaskResponse(response, payload))
        }
        catch (error) {
            this._handleFlaskResponse(error.response)
        }
    }

    _handleFlaskResponse(response, payload=null) {
        // if the server reset access control, request with new credentials
        if (response?.data?.resend) {
            if (response.config.method === 'get') {
                return this.GET('', payload, response.config.url)
                .then(response => response)
            }

            if (response.config.method === 'post') {
                return this.POST('', payload, response.config.url)
                .then(response => response)
            }

            if (response.config.method === 'delete') {
                return this.DELETE('', payload, response.config.url)
                .then(response => response)
            }
        }

        // if the server returned a notification
        let notifications = this._handleServerNotifications(response)
        if (notifications) {
            return notifications
        }

        // if the server returned a redirect
        this._handleRedirect(response, payload)

        return response
    }

    _handleServerNotifications(response) {
        // display any notifications returned from flask
        if (response?.data?.flash) {
            flash(response, this._handleRedirect)
            return response
        }

        if (response?.data?.toast) {
            toastify(response)
        }

        return null
    }

    _handleRedirect(response, payload=null) {
        if (response?.data?.next) {
            if (response.data.next === 'reload') {
                return window.location.reload()
            }

            window.location = response.data.next
        }
    }
}


export default REST
