from flask import Flask
from flask_bootstrap import Bootstrap
from flask_navigation import Navigation

# from .navbar import nav, DarkRenderer
# from flask_nav import register_renderer

from someblog.blog.config.config import TestBuild

app = Flask(__name__)
app.config.from_object(TestBuild)
Bootstrap(app)

# Пусть пока побудет тут костыль, может так и останется
nav = Navigation(app)
from .navbar import nav

# Не трогать
# nav.init_app(app)
# register_renderer(app, 'dark', DarkRenderer)
