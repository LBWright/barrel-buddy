from flask_restful import Resource


class UserRegister(Resource):
    def get(self):
        return {"message": "UserRegister"}


class UserLogin(Resource):
    def get(self):
        return {"message": "UserLogin"}


class UserLogout(Resource):
    def get(self):
        return {"message": "UserLogout"}


class TokenRefresh(Resource):
    def get(self):
        return {"message": "Refresh"}

