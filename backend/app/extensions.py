from flask_restful import Api
from flask_praetorian import Praetorian
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate

api = Api()
guard = Praetorian()
db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()
migrate = Migrate()
