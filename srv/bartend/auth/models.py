from dataclasses import dataclass
import datetime
from marshmallow import ValidationError

from bartend import db
from bartend.auth import schemas
from bartend.auth.auth_api import AuthAPI


@dataclass
class User(db.Model):
    """
    User model
    """
    username: str
    email: str
    date_created: datetime.datetime
    keygen: str
    stamp: datetime.datetime

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    username = db.Column(
        db.String(24),
        unique=True,
        nullable=False,
    )

    email = db.Column(
        db.String(75),
        unique=True,
        nullable=False,
    )

    date_created = db.Column(
        db.DateTime(),
        nullable=False,
        default=datetime.datetime.now(datetime.timezone.utc),
    )

    email_verified = db.Column(
        db.Boolean(),
        default=False,
    )

    perms = db.Column(
        db.String(24),
        nullable=False,
        default='account',
    )

    keygen = db.Column(
        db.String(256),
        unique=False,
    )

    stamp = db.Column(db.DateTime())

    def validate(data):
        try:
            schemas.UserSchema().load(data)
            return True
        except ValidationError:
            return False

    def api(**kwargs):
        return AuthAPI(User, **kwargs)


# def db_create_all():
#     from bartend import app
#     with app.app_context():
#         db.create_all()


# db_create_all()  # you only need to do this once
