import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
if os.path.exists("env.py"): # will only import the env.py file if it exists. (This is to prevent an error when deploying to Heroku)
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes