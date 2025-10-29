"""Application configuration and extensions wiring.

This file sets up Flask, SQLAlchemy, Flask-Migrate, CORS, Flask-RESTful and
Flask-Bcrypt. Environment variables are loaded from a local .env file via
python-dotenv.
"""

# Standard library imports
import os

# Remote library imports
from flask import Flask  # pyright: ignore[reportMissingImports]
from flask_cors import CORS  # pyright: ignore[reportMissingModuleSource]
from flask_migrate import Migrate  # pyright: ignore[reportMissingModuleSource]
from flask_restful import Api  # pyright: ignore[reportMissingImports]
from flask_sqlalchemy import SQLAlchemy  # pyright: ignore[reportMissingImports]
from flask_bcrypt import Bcrypt  # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]

# Load environment from .env (if present)
load_dotenv()

# Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Keep JSON responses readable in development
app.json.compact = False


db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)

bcrypt = Bcrypt(app)
