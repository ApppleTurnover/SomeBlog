import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_navigation import Navigation
from flask_sqlalchemy import SQLAlchemy

from someblog.blog.config import TestBuild

app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config.from_object(TestBuild)
Bootstrap(app)
db = SQLAlchemy(app)

nav = Navigation(app)
from .navbar import nav
