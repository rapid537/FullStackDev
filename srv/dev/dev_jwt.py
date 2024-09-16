from flask import session
from flask_jwt_extended import verify_jwt_in_request
from functools import wraps
import json
from jwt import InvalidTokenError
from werkzeug.exceptions import HTTPException

from bartend import app
from bartend import BASE_CONFIG
from dev.dev_session import extend_access_control


class AuthorizedSessionException(HTTPException):  # pragma: no cover
    code = 403
    description = 'Bad Credentials'


def jwt_required_override(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not jwt_.BYPASS:
            if not session.get('logged_in'):
                raise AuthorizedSessionException
            verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper


@app.before_request
def source_access_control():
    """
    re-issue jwt access tokens if redis session is valid
    """
    if session.get('logged_in', None):
        try:
            verify_jwt_in_request()
        except InvalidTokenError:
            response = extend_access_control()
            response.set_data(json.dumps({'resend': True}))
            return response


class jwt_:  # pragma: no cover
    """
    convenience switch to bypass jwt validation
    for use only in development
    allows for ui/ux-ing with pre-defined jwt/session
    settings are derived from BASE_CONFIG
    """
    BYPASS: bool = BASE_CONFIG.JWT_BYPASS and not BASE_CONFIG.IS_PRODUCTION
    user: object = {
        'username': BASE_CONFIG.SESSION_ID,
        'email': BASE_CONFIG.SESSION_ID_EMAIL,
    }

    def jwt_status():
        devcolors.info_msg()


class devcolors:  # pragma: no cover
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def info_msg():  # pragma: no cover
        if jwt_.BYPASS:
            print(
                ' *',
                devcolors.OKCYAN + 'Info ' + devcolors.ENDC + '@jwt_required',
                devcolors.OKBLUE + 'BYPASS ' + devcolors.ENDC + 'is',
                devcolors.WARNING + 'enabled' + devcolors.ENDC,
            )

        if not jwt_.BYPASS:
            print(
                ' *',
                devcolors.OKCYAN + 'Info ' + devcolors.ENDC + '@jwt_required',
                devcolors.OKBLUE + 'BYPASS ' + devcolors.ENDC + 'is',
                devcolors.OKGREEN + 'not enabled' + devcolors.ENDC,
            )


"""
show current jwt config on server reload
"""
jwt_.jwt_status()
