from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from config import Config  


db = SQLAlchemy()
# migrate = Migrate()

app = Flask(__name__)

app.secret_key = 'watchDogCryptoAPpSecretKey'

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config.from_object(Config)

db.init_app(app)
# migrate.init_app(app, db) 

from app.routes import base, dashboard, auth

app.register_blueprint(auth.bp)
app.register_blueprint(base.bp)
app.register_blueprint(dashboard.bp)
