from flask import Flask, jsonify
from .extensions import api, db, guard, ma, cors, migrate
from app.auth.user import User
from .routes import register_routes


def create_app(env="development"):
    app = Flask(__name__)
    app.debug = True
    app.config["SECRET_KEY"] = "local secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_ACCESS_LIFESPAN"] = {"hours": 24}
    app.config["JWT_REFRESH_LIFESPAN"] = {"days": 30}

    guard.init_app(app, User)
    db.init_app(app)
    migrate.init_app(app, db=db)

    with app.app_context():
        db.create_all()
        db.session.commit()
        ma.init_app(app)

    cors.init_app(app)

    # need a register_routes function
    register_routes(api, app)
    api.init_app(app)

    @app.route("/health")
    def health():
        return jsonify(status="healthy")

    return app


if __name__ == "__main__":
    app.run()
