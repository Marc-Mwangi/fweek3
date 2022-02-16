import os

class Config:
    """
    General configuraion
    """
    MAIL_SERVER= 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS= True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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

config_options = {
    'development': Development ,
    'production': Production
}