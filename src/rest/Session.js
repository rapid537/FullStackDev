import Cookies from 'js-cookie'


export function hasAccessToken() {
    return Cookies.get('csrf_access_token') ? true : false
}
