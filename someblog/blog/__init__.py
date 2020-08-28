from flask import Flask
from flask_bootstrap import Bootstrap
from flask_navigation import Navigation

from someblog.blueprints.blog import blog
from someblog.blog.config import TestBuild

# from .navbar import nav, DarkRenderer
# from flask_nav import register_renderer


app = Flask(__name__)
app.config.from_object(TestBuild)
Bootstrap(app)
app.register_blueprint(blog, url_prefix='/blog')

# Пусть пока побудет тут костыль, может так и останется
nav = Navigation(app)
from .navbar import nav

# Не трогать
# nav.init_app(app)
# register_renderer(app, 'dark', DarkRenderer)
