from someblog.blog import app
from someblog.blog import db

from someblog.blueprints.blog import blog
import someblog.blog.view

app.register_blueprint(blog, url_prefix='/blog')

if __name__ == '__main__':
    app.run()
