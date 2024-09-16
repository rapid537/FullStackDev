import json
import unittest

import config
from bartend import app
from bartend import db
from bartend import redis
from dev.dev_session import create_session


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config.from_object(config.TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        redis.flushdb()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.client = None
        self.app = None


class StudioBaseTest(BaseTestCase):
    def make_req(self, method=None, payload=None, fn=None):
        with self.app.test_request_context(
            data=payload and json.dumps(payload, default=str),
            content_type='application/json',
            method=method or 'get',
        ):
            return fn()

    def make_get_req(self, route=None, query_string=None, headers=None):
        with self.client as client:
            response = client.get(
                f'api/{route}',
                query_string=query_string,
                content_type='application/json',
            )
            return response

    def make_post_req(self, route=None, payload=None, headers=None):
        with self.client as client:
            response = client.post(
                f'api/{route}',
                data=payload and json.dumps(payload, default=str),
                content_type='application/json',
            )
            return response

    def make_delete_req(self, route=None, payload=None, headers=None):
        with self.client as client:
            response = client.delete(
                f'api/{route}',
                data=payload and json.dumps(payload, default=str),
                content_type='application/json',
            )
            return response

    def make_session_req(self, method=None, route=None, payload=None, user=None, jwt_only=None, session_only=None):
        session_response = self.authenticate_user_session(user)

        csrf_token = self._get_cookie_from_response(
            session_response,
            'csrf_access_token',
        ).get('csrf_access_token')

        access_token = self._get_cookie_from_response(
            session_response,
            'access_token_cookie',
        ).get('access_token_cookie')

        headers = {'X-CSRF-TOKEN': csrf_token} if not session_only else {}

        with self.client as client:
            with client.session_transaction() as session:
                if not jwt_only:
                    self._build_user_session(user, session)

            if not session_only:
                client.set_cookie('csrf_access_token', value=csrf_token)
                client.set_cookie('access_token_cookie', value=access_token)

            if method == 'get' or method is None:
                response = client.get(
                    f'api/{route}',
                    query_string=payload and json.dumps(payload, default=str),
                    content_type='application/json',
                    headers=headers,
                )

            if method == 'post':
                response = client.post(
                    f'api/{route}',
                    data=payload and json.dumps(payload, default=str),
                    content_type='application/json',
                    headers=headers,
                )

        return response

    def authenticate_user_session(self, user):
        payload = {
            'username': user.username,
            'email': user.email,
        }

        response = create_session(payload)

        return response

    def _get_cookie_from_response(self, response, cookie_name):
        cookie_headers = response.headers.getlist('Set-Cookie')

        for header in cookie_headers:
            attributes = header.split(';')

            if cookie_name in attributes[0]:
                cookie = {}

                for attr in attributes:
                    split = attr.split('=')
                    cookie[split[0].strip().lower()] = split[1] if len(split) > 1 else True
                return cookie

        return None

    def _build_user_session(self, user, session):
        session['_permanent'] = True
        session['username'] = user.username
        session['email'] = user.email
        session['logged_in'] = True
