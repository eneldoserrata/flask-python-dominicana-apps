__author__ = 'eneldoserrata'

from flask.ext.mail import Mail
from flask.ext.babel import Babel
from flask import Flask, render_template, request, g
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

mail = Mail(app)
babel = Babel(app)

@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['de', 'fr', 'en, es'])

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from views import mod as appModule
app.register_blueprint(appModule)

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)