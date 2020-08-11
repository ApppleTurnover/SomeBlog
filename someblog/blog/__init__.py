from flask import Flask

from someblog.blog.config.config import TestBuild

app = Flask(__name__)
app.config.from_object(TestBuild)
