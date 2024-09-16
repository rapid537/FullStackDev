from flask import request

from bartend import app
from bartend.auth.auth_endpoint import AuthEndpoint
from dev.dev_jwt import jwt_required_override


@app.post('/api/sign_in', endpoint='sign_in')
def sign_in():
    return AuthEndpoint(request=request).sign_in()


@app.post('/api/sign_out', endpoint='sign_out')
def sign_out():
    return AuthEndpoint().sign_out()


@app.post('/api/sign_up', endpoint='sign_up')
def sign_up():
    return AuthEndpoint(request=request).sign_up()


@app.post('/api/confirm_code', endpoint='confirm_code')
def confirm_code():
    return AuthEndpoint(request=request).confirm_code()


@app.get('/api/protected_route', endpoint='protected_route')
@jwt_required_override
def protected_route():
    return AuthEndpoint(request=request).protected_route()
