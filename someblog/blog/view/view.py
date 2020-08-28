from someblog.blog import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html.j2")


@app.route('/blog')
def blog():
    return render_template('blog.html.j2')

