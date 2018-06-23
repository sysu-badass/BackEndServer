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

    

    




