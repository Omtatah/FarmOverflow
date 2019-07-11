import os

class Config:
    """
    This is the class which will contain the general configurations
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = "app/static/photos"

class ProdConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')



class DevConfig(Config):
    SECRET_KEY='absc'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:12345@localhost/test3'
    DEBUG = True

class TestConfig(Config):
    """
    This is the class which will contain the test configurations
    """
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:12345@localhost/test3'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'tests' : TestConfig
}

    