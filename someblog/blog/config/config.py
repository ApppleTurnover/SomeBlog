class TestBuild(object):
    DEBUG = True
    SERVER_NAME = "127.0.0.1:5000"
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
