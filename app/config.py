import os
class Config:
    """
    General configuraion
    """
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://marc:qwerty01@localhost/database'
class Production(Config):
    """
    Production configuration
    """
    pass
class Development(Config):
    """
    Development configuration
    """
    DEBUG = True