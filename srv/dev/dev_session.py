import datetime

from flask import make_response
from flask import session
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_csrf_token

from bartend import BASE_CONFIG


def set_response_cookies(response=None, token=None):
    response = response or make_response()
    max_age = (datetime.timedelta(hours=3))

    response.set_cookie(
        'access_token_cookie',
        httponly=True,
        value=token or create_token(),
        path='/',
        samesite='strict',
        secure=BASE_CONFIG.SECURE_COOKIE,
        domain=BASE_CONFIG.STUDIO_DOMAIN,
        max_age=max_age
    )

    response.set_cookie(
        'csrf_access_token',
        httponly=False,
        value=get_csrf_token(token or create_token()),
        path='/',
        samesite='strict',
        secure=BASE_CONFIG.SECURE_COOKIE,
        domain=BASE_CONFIG.STUDIO_DOMAIN,
        max_age=max_age
    )

    return response


def create_token():
    identity = {
        'username': session.get('username'),
        'email': session.get('email'),
    }
    token = create_access_token(identity=identity)

    return token


def extend_access_control():
    identity = {'username': session.get('username'), 'email': session.get('email')}
    token = create_access_token(identity=identity)

    return set_response_cookies(response=None, token=token)


def create_session(user):
    identity = {'username': user.username, 'email': user.email}
    # set up the response
    response = make_response(identity)
    # set up access tokens
    token = create_access_token(identity=identity)
    # set jwt tokens for client
    set_response_cookies(response=response, token=token)
    # set up server managed session
    make_session(user)

    return response


def make_session(user):
    session.permanent = True
    session['username'] = user.username
    session['email'] = user.email
    session['logged_in'] = True


def make_temp_session(user):
    session.permanent = True
    session['email'] = user.email
    session['temp_session'] = True


def clear_session_data():
    response = make_response()
    session.clear()
    response.delete_cookie('access_token_cookie', path='/', domain=BASE_CONFIG.STUDIO_DOMAIN)
    response.delete_cookie('csrf_access_token', path='/', domain=BASE_CONFIG.STUDIO_DOMAIN)

    return response
