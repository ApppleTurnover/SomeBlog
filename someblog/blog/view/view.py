from flask import render_template, request, redirect, url_for

from someblog.blog import app


@app.route('/')
def index():
    search = request.args.get('search')
    if search:
        return redirect(url_for('blog.index') + f'?search={search}')
    return render_template("index.html")
