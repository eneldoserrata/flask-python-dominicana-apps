from app import db, app
from flask import Blueprint, render_template
from flask.ext.login import login_required
from app.users.models import user_datastore

__author__ = 'eneldoserrata'


mod     = Blueprint('users', __name__, url_prefix='/users')

'''
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='matt@nobien.net', password='password')
    db.session.commit()
'''

# Views
@mod.route('/')
@login_required
def home():
    return render_template('users/users.html')