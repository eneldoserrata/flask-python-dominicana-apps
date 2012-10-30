__author__ = 'eneldoserrata'

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'SecretKeyForSessionSigning'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:marlboro@localhost/mydatabase'

DEFAULT_MAIL_SENDER     = 'eneldoserrata@gmail.com'
SECURITY_REGISTERABLE   = True
SECURITY_CONFIRMABLE    = True
SECURITY_RECOVERABLE    = True

MAIL_SERVER     = 'smtp.gmail.com'
MAIL_PORT       = 465
MAIL_USE_TLS    = False
MAIL_USE_SSL    = True
MAIL_USERNAME   = 'eneldoserrata@gmail.com'
MAIL_PASSWORD   = 'enegis2007'

BABEL_DEFAULT_LOCALE = 'es'
BABEL_DEFAULT_TIMEZONE = 'UTC'


