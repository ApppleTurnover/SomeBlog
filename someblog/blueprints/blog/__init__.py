from flask import Blueprint, render_template, redirect, url_for, flash

from someblog.blog.models import Post

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)


@blog.route('/<slug>')
def post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if post:
        return render_template('blog/post.html', post=post)
    else:
        flash(
            u'<b>404 Not Found</b> The requested post was not found. If you entered the URL manually please check your spelling and try again.',
            'danger')
        return redirect(url_for('blog.index'))
