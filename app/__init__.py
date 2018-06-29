# from flask import Flask
# from flask import session
# from flask import redirect
# from flask import url_for
# from flask import escape
# from flask import request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

# # set the secret key.  keep this really secret:
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from werkzeug.utils import import_string
from app.admin.admin import iden_loaded
from flask_principal import identity_loaded 



# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123456@localhost/rbac'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SECRET_KEY']='123'

db = SQLAlchemy()

principals = Principal()

#用户认证
login_manager = LoginManager()
#配置用户认证信息

#认证加密程度
login_manager.session_protection='strong'

# @login_manger.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

blueprints = [
    'app.views.sample_view:auth',
]

import app.database.models

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
 
    # Load extensions
    db.app = app
    db.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)
 
    # Load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)
    
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        iden_loaded(sender, identity)
 
    return app
