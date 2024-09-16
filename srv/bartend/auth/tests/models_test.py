from bartend.auth.models import User
from bartend.auth.tests.auth_fixtures.auth import TestUser
from tests.tests import StudioBaseTest


class TestUserModel(StudioBaseTest):
    def test_user_validate(self):
        data = {
            'username': 'test_user',
            'email': 'test_user@mail.com',
        }

        is_valid = User.validate(data)
        assert is_valid is True

        data['username'] = None
        is_valid = User.validate(data)
        assert is_valid is False


class TestUserModelApi(StudioBaseTest):
    def test_user_get_or_create(self):
        user = User.query.filter_by(username='test_user').first()
        assert user is None

        user = User.api().get_or_create(
            **TestUser.item_to_dict(TestUser.generate('test_user'))
        )
        assert user

        user = User.api().get_or_create(username='test_user')
        assert user

    def test_user_update_or_create(self):
        user = User.query.filter_by(username='test_user').first()
        assert user is None

        User.api().update_or_create(
            **TestUser.item_to_dict(TestUser.generate('test_user'))
        )
        user = User.query.filter_by(username='test_user').first()
        assert user

        User.api().update_or_create(username='test_user', email='updated@mail.com')
        user = User.query.filter_by(username='test_user').first()
        assert user.email == 'updated@mail.com'
