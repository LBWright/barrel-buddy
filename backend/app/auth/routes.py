BASE_ROUTE = "auth"


def register_routes(api, app, root="api"):
    from .user.controller import UserListResource, UserResource
    from .controller import UserLogin, UserLogout, UserRegister, TokenRefresh

    api.add_resource(UserListResource, f"/{root}/{BASE_ROUTE}/users")
    api.add_resource(UserResource, f"/{root}/{BASE_ROUTE}/users/<int:id>")
    api.add_resource(UserLogin, f"/{root}/{BASE_ROUTE}/login")
    api.add_resource(UserLogout, f"/{root}/{BASE_ROUTE}/logout")
    api.add_resource(UserRegister, f"/{root}/{BASE_ROUTE}/register")

