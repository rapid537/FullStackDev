import coverage
from flask import request

from bartend import app
from bartend import db
from bartend import redis
from bartend.auth.tests.auth_fixtures.auth import TestUser
from dev.dev_session import create_session
from endpoint.studio_endpoint import StudioEndpoint


cov = coverage.Coverage(context='cy_context')


class CyEndpoint(StudioEndpoint):
    def authenticate_user(self):
        class user:
            username = self.data['username']
            email = self.data['email']

        return create_session(user)


@app.post('/api/cy_db_setup', endpoint='cy_db_setup')
def cy_db_setup():
    db.create_all()
    return 'ok', 200


@app.post('/api/cy_db_teardown', endpoint='cy_db_teardown')
def cy_db_teardown():
    redis.flushdb()
    db.session.remove()
    db.drop_all()
    return 'ok', 200


@app.get('/api/coverage_start', endpoint='coverage_start')
def coverage_start():
    cov.start()
    return 'ok', 200


@app.get('/api/coverage_stop', endpoint='coverage_stop')
def coverage_stop():
    cov.stop()
    cov.save()
    return 'ok', 200


@app.post('/api/cy_authenticate_user', endpoint='cy_authenticate_user')
def cy_authenticate_user():
    return CyEndpoint(request=request).authenticate_user()


@app.post('/api/cy_create_test_user', endpoint='cy_create_test_user')
def cy_create_test_user():
    new_user = TestUser.generate('test_user')
    TestUser.db_add(new_user)
    return 'ok', 200
