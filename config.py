import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    # 'mysql+pymysql://root:root123456@db/rbac' 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or\
            'mysql+pymysql://root:root123456@db/rbac' 

class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or\
            'mysql+pymysql://root:root123456@localhost/rbac'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or\
            'mysql+pymysql://root:root123456@localhost/rbac'

config = {
            'development':DevelopmentConfig,
            'testing':TestingConfig,
            'production':ProductionConfig,
            'default':DevelopmentConfig
        }
