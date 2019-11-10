from flask import jsonify, request
from flask_restful import Resource
from app.extensions import guard


class UserRegister(Resource):
    def get(self):
        return {"message": "UserRegister"}


class UserLogin(Resource):
    def post(self):
        req = request.get_json(force=True)
        username = req.get("username", None)
        password = req.get("password", None)
        user = guard.authenticate(username, password)
        ret = {"access_token": guard.encode_jwt_token(user)}
        return (ret, 200)


class UserLogout(Resource):
    def get(self):
        return {"message": "UserLogout"}


class TokenRefresh(Resource):
    def get(self):
        return {"message": "Refresh"}

