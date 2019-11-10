from datetime import datetime
from app.extensions import db, guard


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    # separated by CSV right now
    roles = db.Column(db.Text, default="user")
    is_active = db.Column(db.Boolean, default=True, server_default="true")
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<User username={self.username} >"

    @property
    def rolenames(self):
        try:
            return self.roles.split(",")
        except Exception:
            return []

    @property
    def identity(self):
        return self.id

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def is_valid(self):
        return self.is_active

    def set_password(self, raw_password):
        self.password = guard.hash_password(raw_password)

    def save(self):
        db.session.add(self)
        db.session.commit()
