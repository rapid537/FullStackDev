from flask import json
from flask import make_response


class BaseResponse:
    def return_response(self):
        """
        build the response data and return to front-end
        """
        if not self.response and not self.data:
            return make_response('OK', 200)

        # set default status
        status_code = 500 if self.data.get('err') else 200

        # override status_code if kwargs['status_code']
        if self.data.get('status_code'):
            status_code = self.data.get('status_code')

        # merge response data if both exist
        if self.response and self.data:
            response_data = {}

            if self.response.data:
                response_data = json.loads(self.response.data)

            response_data.update(self.data)
            self.response.set_data(json.dumps(response_data))

        # return generic data, a predefined make_response() object, or kwargs
        return make_response(self.response or self.data, status_code)


class StudioResponse(BaseResponse):
    """
    a custom class for handling response
    """

    def __new__(self, response=None, **kwargs):
        """
        @override
        ignores __init__ and returns a response object
        """

        # generic response or predefined make_response()
        self.response = response
        self.data = kwargs
        return self.return_response(self)
