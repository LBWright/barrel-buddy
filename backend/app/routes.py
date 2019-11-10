def register_routes(api, app, root="api"):
    from app.auth.routes import register_routes as attach_auth

    attach_auth(api, app)
