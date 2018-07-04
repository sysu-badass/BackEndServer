from flask import Flask, current_app, request, session, redirect, url_for, abort
from flask import Blueprint
from flask_login import LoginManager, login_user, logout_user, \
     login_required, current_user
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required
from flask_principal import Principal, Identity, AnonymousIdentity, \
     identity_changed

from app import login_manager
from app.database.dao import UserDao

from app.admin.admin import ModIdentityPermission
from app.admin.admin import AccessUrlPermission

auth = Blueprint('auth', __name__, url_prefix='')

from app.database.models import User

@login_manager.user_loader
def load_user(userid):
    # Return an instance of the User model
    return UserDao.get_user_by_id(userid)

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = UserDao.get_user(username)

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    # user.is_authenticated = request.form['password'] == user.password

    return user

@auth.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + str(current_user.id)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # A hypothetical login form that uses Flask-WTF
    # form = LoginForm()

    # Validate form input
    if request.method == 'POST':
        username = request.form.get('user_id')
        password = request.form.get('user_password')

        #if form.validate_on_submit():
            # Retrieve the user from the hypothetical datastore
        user = UserDao.get_user(username)
            # Compare passwords (use password hashing production)
        if password == user.password:
                # Keep the user info in the session using Flask-Login
            login_user(user)
                # Tell Flask-Principal the identity changed
            identity_changed.send(current_app._get_current_object(),
                                    identity=Identity(user.id))

            return redirect(url_for('auth.protected'))

    return ''''' 
        <form action="#" method="POST"> 
            <span>请输入账号</span> 
            <input type="text" name="user_id" id="user_id" placeholder="name"> 
            <span>请输入密码</span> 
            <input type="password" name="user_password" id="user_password" placeholder="password"> 
            <input type="submit" name="submit"> 
       </form> 
        '''

@auth.route('/logout')
@login_required
def logout():
    # Remove the user information from the session
    logout_user()

    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())

    return redirect(url_for('auth.protected'))

@auth.route('/edit/<username>')
def edit(username):
    identityPermission = ModIdentityPermission(username)
    urlPermission = AccessUrlPermission('/edit')

    if (urlPermission.can() and identityPermission.can()):
        return "edit"
    print("fail")
    print(current_user.roles)
    for role in current_user.roles:
        print(role.permissions)
    print(current_user.username)
    print(identityPermission)
    print(urlPermission)
    abort(403)