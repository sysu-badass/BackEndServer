from app import db
from app.database.models import User
from app.database.models import Role
from app.database.models import Permission
from app import create_app
from config import config
import pymysql

config_name = 'development'
app = create_app(config[config_name])

db.create_all()
print(db)
user = User(id='lisi',username='lisi', password='123')
role = Role(rolename='teacher')
permission = Permission(url='/edit')

role.permissions.append(permission)
user.roles.append(role)

db.session.add(user)
db.session.commit()
