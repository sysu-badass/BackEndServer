from rbac.models import User
from rbac.models import Role
from rbac.models import Permission
from server import db

class Admin:
    def hasPermission(self, role, permission):
        plist = self.perm2list(role.permissions)
        isPermitted = self.match(permission.url, plist)
        return isPermitted

    # todo
    def match(self, url, urlList):
        return url in urlList

    def perm2list(self, permissions):
        result = []
        for permission in permissions:
            result.append(permission.url)
        return result

    # def addUser(self, username, password):
    #     usr = User(username=username, password=password)
    #     db.session.add(usr)
    #     db.session.commit()
    
    # def addRole(self, rolename):
    #     role = Role(rolename=rolename)
    #     db.session.add(role)
    #     db.session.commit()
    
    # def addPermission(self, url):
    #     permission = Permission(url=url)
    #     db.session.add(permission)
    #     db.session.commit()
    
    # def addPermToRole(self, url, rolename):
    #     permission = Permission(url=url)
    #     role = Role(rolename=rolename)
    #     role

    




