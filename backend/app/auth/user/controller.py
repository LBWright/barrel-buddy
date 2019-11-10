from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_praetorian import auth_required, roles_required, current_user
from .schema import UserSchema
from .model import User

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserListResource(Resource):
    def get(self):
        users = User.get_all()
        return {"data": users_schema.dump(users)}

    def post(self):
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return ({"error": err.messages}, 400)

        user.set_password(user.password)
        user.save()

        return ({"data": user_schema.dump(user)}, 201)


class UserResource(Resource):
    def get(self, id):
        user = User.find_by_id(id)

    def put(self, id):
        return {"user": "this will update a single user"}

    def delete(self, id):
        return {"message": "this will delete a user"}

