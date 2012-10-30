from flask import Blueprint, render_template
from flask.ext.login import login_required
from flask.ext import babel

__author__ = 'eneldoserrata'

mod = Blueprint('app', __name__, url_prefix='/')


@mod.route('/')
def home():
    return render_template('index.html', hola = "hello")