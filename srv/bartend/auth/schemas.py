from marshmallow import fields
from marshmallow import Schema
from marshmallow import validate


class AuthBaseSchema(Schema):
    """
    validators
    """
    username = fields.Str(
        validate=validate.Length(min=2, max=64),
        required=True,
    )

    email = fields.Email(
        validate=validate.Length(max=127),
        required=True,
    )

    date_created = fields.DateTime()


class UserSchema(AuthBaseSchema):
    pass


class AuthSchema(AuthBaseSchema):
    pass
