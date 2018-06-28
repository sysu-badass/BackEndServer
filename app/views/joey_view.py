from flask import Flask, current_app, request, session, redirect, url_for, abort
from flask_login import LoginManager, login_user, logout_user, \
     login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, \
     identity_changed
from flask_restful import reqparse, abort, Api, Resource

from app import login_manager, api
from app.database.dao import UserDao, OrderHistory, OrderHistoryItem, \
     Restaurant, Food, Order, OrderItem

from app.service.joey_service import Customer_service, Admin_service

from app.admin.admin import ModIdentityPermission
from app.admin.admin import AccessUrlPermission

parser = reqparse.RequestParser()
parser.add_argument('user_id')
parser.add_argument('user_password')
parser.add_argument('restaurant_id')
parser.add_argument('URL')
parser.add_argument('order_history_id')
parser.add_argument('date')
parser.add_argument('desk_number')
parser.add_argument('total_price')
parser.add_argument('order_history_item_id')
parser.add_argument('number')
parser.add_argument('description')
parser.add_argument('image')
parser.add_argument('price')
parser.add_argument('restaurant_admin_id')
parser.add_argument('restaurant_admin_password')
parser.add_argument('restaurant_name')
parser.add_argument('restaurant_information')
parser.add_argument('food_id')
parser.add_argument('name')
parser.add_argument('food_type')
parser.add_argument('available')
parser.add_argument('order_item_id')
parser.add_argument('order_id')


#顾客登录的话，如果数据库里没有相关账号密码，则创建一个
class Customer_login(Resource):
    def post(self):
        data = parser.parse_args()
        if UserDao.get_user_by_id(data['user_id'])

#顾客查看订单列表
class Customer_orders(Resource):
    def get(self):
        data = parser.parse_args()

#顾客查看订单
class Customer_order(Resource):
    def get(self):
        data = parser.parse_args()

#顾客查看订单中的菜品的信息
class Customer_order_food(Resource):
    def get(self):
        data = parser.parse_args()

#顾客查看菜单
class Customer_menu(Resource):
    def get(self):
        data = parser.parse_args()

#顾客查看菜单中菜品的信息
class Customer_menu_food(Resource):
    def get(self):
        data = parser.parse_args()

#顾客选择支付方式
class Customer_payment(Resource):
    def post(self):
        data = parser.parse_args()

#餐厅管理员注册
class admin_join(Resource):
    def post(self):
        data = parser.parse_args()

#餐厅管理员登录
class admin_login(Resource):
    def post(self):
        data = parser.parse_args()()

#餐厅管理员操作餐厅订单列表
class admin_orders(Resource):
    def get(self):
        data = parser.parse_args()()

    def post(self):
        data = parser.parse_args()()

#餐厅管理员操作餐厅订单
class admin_order(Resource):
    def get(self):
        data = parser.parse_args()()

    def put(self):
        data = parser.parse_args()()

    def delete(self):
        data = parser.parse_args()()

#餐厅管理员操作餐厅订单中的菜品
class admin_order_food(Resource):
    def get(self):
        data = parser.parse_args()()

#餐厅管理员操作餐厅菜单列表
class admin_menu(Resource):
    def get(self):
        data = parser.parse_args()()

    def post(self):
        data = parser.parse_args()()

    def delete(self):
        data = parser.parse_args()()

#餐厅管理员操作餐厅菜单中的菜品
class admin_menu_food(Resource):
    def get(self):
        data = parser.parse_args()()

    def put(self):
        data = parser.parse_args()()

    def delete(self):
        data = parser.parse_args()

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
