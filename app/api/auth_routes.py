from flask import Blueprint, jsonify, session, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import RegisterForm
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint('auth', __name__)

def validation_errors_to_error_messages(validation_errors):
    # turn WTForms validation errors into list
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    # authenticates user
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    # logs in user
    form = LoginForm()
    # csrf_token from request cookie into form so validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # add user to session => logged in
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    # logs out user
    logout_user()
    return {'message': 'user logged out'}


@auth_routes.route('/register', methods=['POST'])
def sign_up():
    # create new user and logs them in
    form = RegisterForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            favorite_color=form.data['favorite_color'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    # returns unauthorized JSON when flask-login authentication fails
    return {'errors': ['unauthorized']}, 401
