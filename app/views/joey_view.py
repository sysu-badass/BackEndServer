from flask import Flask, current_app, request, session, redirect, url_for, abort
from flask import Blueprint
from flask_login import LoginManager, login_user, logout_user, \
     login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, \
     identity_changed

from app import login_manager, api
from app.database.dao import UserDao

from app.admin.admin import ModIdentityPermission
from app.admin.admin import AccessUrlPermission

#顾客登录的话，如果数据库里没有相关账号密码，则创建一个
class Customer_login(Resource):
    pass

#顾客查看订单列表
class Customer_orders(Resource):
    pass

#顾客查看订单
class Customer_order(Resource):
    pass

#顾客查看订单中的菜品的信息
class Customer_order_food(Resource):
    pass

#顾客查看菜单
class Customer_menu(Resource):
    pass

#顾客查看菜单中菜品的信息
class Customer_menu_food(Resource):
    pass

#顾客选择支付方式
class Customer_payment(Resource):
    pass

#餐厅管理员注册
class admin_join(Resource):
    pass

#餐厅管理员登录
class admin_login(Resource):
    pass

#餐厅管理员操作餐厅订单列表
class admin_orders(Resource):
    pass

#餐厅管理员操作餐厅订单
class admin_order(Resource):
    pass

#餐厅管理员操作餐厅订单中的菜品
class admin_order_food(Resource):
    pass

#餐厅管理员操作餐厅菜单列表
class admin_menu(Resource):
    pass

#餐厅管理员操作餐厅菜单中的菜品
class admin_menu_food(Resource):
    pass

api.add_resource(Customer_login, '/users/login')
api.add_resource(Customer_menu, '/users/<user_id>/<restaurant_id>/menu')
api.add_resource(Customer_menu_food, '/users/<user_id>/<restaurant_id>/menu/<food_id>')
api.add_resource(Customer_orders, '/users/<user_id>/<restaurant_id>/orders')
api.add_resource(Customer_order, '/users/<user_id>/<restaurant_id>/orders/<order_id>')
api.add_resource(Customer_order_food, '/users/<user_id>/<restaurant_id>/orders/<order_id>/<food_id>')
api.add_resource(Customer_payment, '/users/<user_id>/<restaurant_id>/payment')
api.add_resource(admin_join, '/restaurants/join')
api.add_resource(admin_login, '/restaurants/login')
api.add_resource(admin_orders, '/restaurants/<restaurant_id>/orders')
api.add_resource(admin_order, '/restaurants/<restaurant_id>/orders/<order_id>')
api.add_resource(admin_order_food, '/restaurants/<restaurant_id>/orders/<order_id>/<food_id>')
api.add_resource(admin_menu, '/restaurants/<restaurant_id>/menu')
api.add_resource(admin_menu_food, '/restaurants/<restaurant_id>/menu/<food_id>')
