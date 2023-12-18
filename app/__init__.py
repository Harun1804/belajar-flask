from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # database instance
migrate = Migrate(app, db) # migration engine instance

from app.model import user, dosen, mahasiswa
from app import routes