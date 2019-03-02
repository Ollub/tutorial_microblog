import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mail server configuration for error handling
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['orlov.o@mail.ru']
    #pagination
    POSTS_PER_PAGE = 25
    #translation
    LANGUAGES = ['en', 'ru']
    YA_KEY = 'trnsl.1.1.20190224T072926Z.b67620fcaa39011a.670b6351a26efb3b442511116be06521d6ed0f15'
    #search engine
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
