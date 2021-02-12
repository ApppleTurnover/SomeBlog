class TestBuild(object):
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/test.db?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
