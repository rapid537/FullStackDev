import datetime

from bartend import bcrypt
from bartend.auth.models import User
from tests.fixtures.base import StudioBaseFixture


class TestUser(StudioBaseFixture):
    def generate(user_data, keygen=None, stamp=None, email_verified=False):
        user = User(
            username=user_data,
            email=f'{user_data}@mail.com',
            keygen=keygen and bcrypt.generate_password_hash(keygen).decode('utf-8'),
            stamp=stamp or datetime.datetime.now(datetime.timezone.utc),
            date_created=datetime.datetime.now(datetime.timezone.utc),
            email_verified=email_verified,
        )

        return user
