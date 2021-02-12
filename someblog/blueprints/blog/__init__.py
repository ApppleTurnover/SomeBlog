import requests
from flask import Blueprint, render_template, \
    redirect, url_for, flash, request

from someblog.blog import db
from someblog.blog.models import Post, Tag
from someblog.blueprints.blog.forms import PostForm

cat_fact = requests.get('https://cat-fact.herokuapp.com/facts/random').json()['text']
blog = Blueprint('blog', __name__, template_folder='templates', url_prefix='/api')


@blog.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print("Wrong")

        return redirect(url_for('blog.index'))

    form = PostForm()
    return render_template('blog/create_post.html', form=form)


@blog.route('/')
def index():
    search = request.args.get('search')
    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.body.contains(search))
        try:
            posts[0]
        except IndexError:
            flash(u'<b>404 Not Found</b> The requested posts were not found. If you entered the '
                  u'URL manually please check your spelling and try again.', 'danger')
            return redirect(url_for('blog.index'))
    else:
        posts = Post.query.order_by(Post.created.desc())

    return render_template('blog/index.html', posts=posts, cat_fact=cat_fact)


@blog.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if post:
        tags = post.tags
        return render_template('blog/post.html', post=post, tags=tags)
    else:
        flash(u'<b>404 Not Found</b> The requested post was not found. If you entered the '
              u'URL manually please check your spelling and try again.', 'danger')
        return redirect(url_for('blog.index'))


@blog.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    if tag:
        posts = tag.posts.all()
        return render_template('blog/tag.html', posts=posts, tag=tag)
    else:
        flash(u'<b>404 Not Found</b> The requested tag was not found. If you entered the '
              u'URL manually please check your spelling and try again.', 'danger')
        return redirect(url_for('blog.index'))
