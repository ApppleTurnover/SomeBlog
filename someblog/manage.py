from someblog.blog import app, manager

from someblog.blueprints.blog import blog

app.register_blueprint(blog, url_prefix='/blog')

if __name__ == '__main__':
    manager.run()
