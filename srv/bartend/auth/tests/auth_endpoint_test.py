from bartend.auth.routes import sign_in
from bartend.auth.tests.auth_fixtures.auth import TestUser
from tests.tests import StudioBaseTest


class TestAuthEndpoint(StudioBaseTest):
    pass


class TestSignIn(TestAuthEndpoint):
    def test_sign_in(self):
        test_user_1 = TestUser.generate('test_user_1')
        TestUser.db_add(test_user_1)

        payload = {'email': test_user_1.email}

        response = self.make_req('post', payload, sign_in).get_json()
        assert response['status_code'] == 202
        assert response['next'] == '/auth/sign-up'

        test_user_2 = TestUser.generate('test_user_2', email_verified=True)
        TestUser.db_add(test_user_2)

        payload = {'email': test_user_2.email}

        response = self.make_req('post', payload, sign_in).get_json()
        assert response['status_code'] == 201
        assert response['next'] == '/auth/confirm-code'
