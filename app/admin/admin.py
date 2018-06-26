from collections import namedtuple
from functools import partial

from flask_login import current_user
from flask_principal import identity_loaded, Permission, RoleNeed, UserNeed

IdentityNeed = namedtuple('identity', ['method', 'value'])
ModIdentityNeed = partial(IdentityNeed, 'mod')

class ModIdentityPermission(Permission):
    def __init__(self, username):
        need = ModIdentityNeed(username)
        super(ModIdentityPermission, self).__init__(need)

RestaurantNeed = namedtuple('restaurant', ['method', 'value'])
ModRestaurantNeed = partial(RestaurantNeed, 'modRestaurantNeed')

class ModRestaurantPermission(Permission):
    def __init__(self, id):
        need = ModRestaurantNeed(id)
        super(ModRestaurantPermission, self).__init__(need)

UrlNeed = namedtuple('url', ['method', 'value'])
AccessUrlNeed = partial(UrlNeed, 'accessUrl')

class AccessUrlPermission(Permission):
    def __init__(self, url):
        need = AccessUrlNeed(url)
        super(AccessUrlPermission, self).__init__(need)

def iden_loaded(sender, identity):
    identity.user = current_user
    print('on_identity_loaded')

    if hasattr(current_user, 'id'):
        print('1')
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        print('2')
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.rolename))
            if hasattr(role, 'permissions'):
                print('3')
                for permission in role.permissions:
                    identity.provides.add(AccessUrlNeed(permission.url))

    if hasattr(current_user, 'username'):
        identity.provides.add(ModIdentityNeed(current_user.username))
    
    if hasattr(current_user, 'restaurants'):
        for restaurant in current_user.restaurants:
            identity.provides.add(ModRestaurantNeed(current_user.restaurants.id))















    # def hasPermission(self, role, permission):
    #     plist = self.perm2list(role.permissions)
    #     isPermitted = self.match(permission.url, plist)
    #     return isPermitted

    # # todo
    # def match(self, url, urlList):
    #     return url in urlList

    # def perm2list(self, permissions):
    #     result = []
    #     for permission in permissions:
    #         result.append(permission.url)
    #     return result

    

    




