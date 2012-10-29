from flask import Blueprint, render_template
from flask.ext.login import login_required

__author__ = 'eneldoserrata'

mod = Blueprint('app', __name__, url_prefix='/')

# Views
@mod.route('/')
@login_required
def home():
    return render_template('index.html')