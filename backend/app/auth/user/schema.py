from app.extensions import ma
from .model import User


class UserSchema(ma.ModelSchema):
    """User schema"""

    class Meta:
        model = User
        load_only = ("password",)
        dump_only = ("id",)

