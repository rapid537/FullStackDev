from flask import session

from dev.dev_jwt import jwt_
from endpoint.response.studio_response import StudioResponse


class Endpoint:
    def __init__(self, request=None, **kwargs):
        self.respond = StudioResponse
        self.request = request
        self.kwargs = kwargs
        self.data = request and self._request_data()
        self.user = jwt_.user if jwt_.BYPASS else {**session}

    def _request_data(self):
        data = None

        if self.request.method == 'GET':
            data = self.GET()

        if self.request.method == 'POST':
            data = self.POST()

        if self.request.method == 'DELETE':
            data = self.DELETE()

        return data

    def GET(self):
        if self.request.args:
            return self.request.args.get('payload') or self.request.args or None

    def POST(self):
        if self.request.get_json():
            return self.request.get_json().get('payload') or self.request.get_json()

    def DELETE(self):
        if self.request.get_json():
            return self.request.get_json().get('payload') or self.request.get_json()

    def flash(self, kwargs=None) -> dict:
        if not kwargs.get('buttons'):
            kwargs.update({'buttons': {'cancel': False, 'confirm': True}})

        return kwargs

    def toast(self, kwargs=None) -> dict:
        return kwargs


class StudioEndpoint(Endpoint):
    pass
