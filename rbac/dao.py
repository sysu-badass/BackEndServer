from rbac.models import db
from rbac.models import User
from rbac.models import Role
from rbac.models import Permission
from database.dao_helper import DaoHelper

class Dao:
    def get_user_by_id(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    def get_user(self, username):
        user = User.query.filter_by(username=username).first()
        return user
    
    def get_role(self, rolename):
        role = Role.query.filter_by(rolename=rolename).first()
        return role
    
    def get_permission(self, url):
        permission = Permission.query.filter_by(url=url).first()
        return permission

    def get_user_roles(self, username):
        return self.get_user(username).roles
    
    def get_role_permissions(self, rolename):
        return self.get_role(rolename).permissions

    def add_user(self, username, password):
        usr = User(username=username, password=password)
        flag = DaoHelper._add_comit(db, usr)
        return flag

    def add_role(self, rolename):
        role = Role(rolename=rolename)
        flag = DaoHelper._add_comit(db, role)
        return flag
    
    def add_permission(self, url):
        permission = Permission(url=url)
        flag = DaoHelper._add_comit(db, permission)
        return flag
    
    def add_perm_to_role(self, url, rolename):
        permission = self.get_permission(url)
        role = self.get_role(rolename)
        flag = True
        if permission and role:
            role.permissions.append(permission)
            flag = DaoHelper._add_comit(db, role)
        else:
            flag = False
        return flag

    def add_role_to_user(self, rolename, username):
        user = self.get_user(username)
        role = self.get_role(rolename)
        flag = True
        if user and role:
            user.roles.append(role)
            flag = DaoHelper._add_comit(db, user)
        else:
            flag = False
        return flag
    
    def update_user(self, user_id, key, value):
        user = self.get_user_by_id(user_id)
        flag = DaoHelper._update_commit(db, user, key, value)
        return flag
    
    def del_user(self, user_id):
        user = self.get_user_by_id(user_id)
        flag = DaoHelper._del_commit(db, user)
        return flag