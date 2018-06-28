from flask import Flask, current_app, request, session, redirect, url_for, abort
from flask_login import LoginManager, login_user, logout_user, \
     login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, \
     identity_changed
from flask_restful import reqparse, abort, Api, Resource

from app import login_manager, api
from app.database.dao import UserDao, OrderHistory, OrderHistoryItem, \
     Restaurant, Food, Order, OrderItem

from app.service.joey_service import service

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
#action='append'可以使得parser的key得到多个值
parser.add_argument('food_id', action='append')
parser.add_argument('name')
parser.add_argument('food_type')
parser.add_argument('available')
parser.add_argument('order_item_id')
parser.add_argument('order_id')
parser.add_argument('orders')
parser.add_argument('foods')
parser.add_argument('order_items')


#顾客登录的话，如果数据库里没有相关账号密码，则创建一个
class Customer_login(Resource):
    def post(self):
        data = parser.parse_args()
        customer = UserDao.get_user_by_id(data['user_id'])
        if customer != None:
            if service.hash_password_verify(data['user_password'], customer.password, customer.id):
                return {'URL': "/users/%d/%d/menu"%(customer.id, data['restaurant_id'])}, 200
            else:
                return {'message': 'login error'}, 400
        else:
            #加密密码，可用service.hash_password_verify(password, hash_password, account)认证
            password = service.hash_password(data['user_password'], data['user_id'])
            UserDao.add_user(data['user_id'], data['username'], password)
            return {'URL': "/users/%d/%d/menu"%(data['user_id'], data['restaurant_id'])}, 200

#顾客查看订单列表
class Customer_orders(Resource):
    def get(self):
        data = parser.parse_args()
        customer_orders = OrderHistoryDao.get_user_orders(data['user_id'], data['restaurant_id'])
        return [customer_order.__json__ for customer_order in customer_orders], 200

#顾客查看订单
class Customer_order(Resource):
    def get(self):
        data = parser.parse_args()
        customer_order_items = OrderHistoryDao.get_order_history_items(id=data['order_history_id'])
        if customer_order_items == None:
            return {'message': "No such order exists"}, 400
        return [customer_order_item.__json__ for customer_order_item in customer_order_items], 200

#顾客查看订单中的菜品的信息
class Customer_order_food(Resource):
    def get(self):
        data = parser.parse_args()
        customer_order_items = OrderHistoryItemDao.get_order_history_items(id=data['order_history_id'])
        for customer_order_item in customer_order_items:
            food = FoodDao.get_food_by_name(customer_order_item.name)
            if food != None:
                return food.__json__, 200
        return {'message': "No such food exists in this order"}, 400

#顾客查看菜单
class Customer_menu(Resource):
    def get(self):
        foods = FoodDao.get_foods(data['restaurant_id'])
        return [food.__json__ for food in foods]

#顾客查看菜单中菜品的信息
class Customer_menu_food(Resource):
    def get(self):
        data = parser.parse_args()
        food = FoodDao.get_food_by_id(data['food_id'])
        if food == None:
            return {"message": "No such food exists in this menu"}, 400
        else:
            return food.__json__, 200


#返回支付方法对应的网站,这是一个json数组类型
class Customer_payment(Resource):
    def get(self):
        return {[{"URL": "example.com"}]}, 200

#餐厅管理员注册
class admin_join(Resource):
    def post(self):
        data = parser.parse_args()
        admin = UserDao.get_user_by_id(data['restaurant_admin_id'])
        restaurant = RestaurantDao.get_restaurant_by_id(data['restaurant_id'])
        if admin != None:
            return {"message": "This administrator already exists"}, 400
        password = service.hash_password(data['restaurant_admin_password'], data['restaurant_admin_id'])
        UserDao.add_user(data['restaurant_admin_id'], data['restaurant_admin_password'])
        #如果餐厅的ID不存在，则创建一个
        if restaurant == None:
            RestaurantDao.add_restaurant(data['restaurant_id'], data['restaurant_admin_id'])
        return {'URL': '/restaurants/%d/menu'%(data['restaurant_id'])}, 200

#餐厅管理员登录
class admin_login(Resource):
    def post(self):
        data = parser.parse_args()
        admin = UserDao.get_user_by_id(data['user_id'])
        if admin != None:
            if service.hash_password_verify(data['restaurant_admin_password'], admin.password, admn.id):
                #更新餐厅的资料
                key = ['id', 'name', 'information', 'user_id']
                value = [data['restaurant_id'], data['restaurant_name'], data['restaurant_information'], data['restaurant_admin_id']]
                RestaurantDao.update_restaurant(data['restaurant_id'], key, value)
                return {'URL': "/restaurants/%d/menu"%(data['restaurant_id'])}, 200
        return {'message': 'Login error'}, 400


#餐厅管理员操作餐厅订单列表
class admin_orders(Resource):
    def get(self):
        data = parser.parse_args()
        restruant_orders = OrderDao.get_restaurant_orders(data['restaurant_id'])
        return {'orders': [restaurant_orders.__json__ for restaurant_order in restaurant_orders]}, 200

    def post(self):
        data = parser.parse_args()
        #orders是list类型的，里面的元素是orderItem
        orders = data['order_items']
        for i in range(len(orders)):
            order = OrderItemDao.get_food_by_id(foods[i]['food_id'])
            #如果提交的food的信息数据库里面有相同id，则更新它
            if food != None:
                keys, values = service.get_keys_values(foods[i])
                FoodDao.update_food(foods[i]['food_id'], keys, values)
            #如果没有则创建
            else:
                FoodDao.add_food(foods[i]['food_id'], foods[i]['name'], foods[i]['price'],
                                foods[i]['food_type'], foods[i]['description'],
                                foods[i]['image'], foods[i]['available'], foods[i]['restaurant_id'])
        return {"URL": "/restaurants/%d/orders/%d"%()}, 200

#餐厅管理员操作餐厅订单
class admin_order(Resource):
    def get(self):
        data = parser.parse_args()
        order_items = OrderItemDao.get_order_items(data['order_id'])
        return {'order_items': [order_item.__json__ for order_item in order_items]}

    def put(self, restaurant_id, order_id):
        data = parser.parse_args()
        order_items = data['order_items']
        for i in range(len(order_items)):
            order_item = OrderItemDao.get_order_item(order_items[i]['order_item_id'])
            #如果提交的food的信息数据库里面有相同id，则更新它
            if order_item != None:
                keys, values = service.get_keys_values(order_items[i])
                OrderItemDao.update_food(foods[i]['food_id'], keys, values)
            #如果没有则创建
            else:
                OrderItemDao.add_food(order_items[i]['order_item_id'], order_items[i]['number'], order_items[i]['name'],
                                order_items[i]['description'], order_items[i]['image'],
                                order_items[i]['price'], order_items[i]['order_id'])
        return {"URL": "/restaurants/%d/orders/%d"%(restaurant_id, order_id)}, 200

    def delete(self):
        data = parser.parse_args()
        if OrderItemDao.get_order_item(data['order_items']['order_item_id']) != None:
            OrderItemDao.del_order_item(data['order_items']['order_item_id'])
            return 204
        else:
            return {"message": "The order item is not in the order"}, 400

#餐厅管理员操作餐厅订单中的菜品
class admin_order_food(Resource, restaurant_id, food_id):
    def get(self):
        return {"URL": "/restaurants/%d/menu/%d"%(restaurant_id, food_id)}

#餐厅管理员操作餐厅菜单列表
class admin_menu(Resource):
    def get(self):
        data = parser.parse_args()
        foods = FoodDao.get_foods(data['restaurant_id'])
        return {'foods': [food.__json__ for food in foods]}

    def post(self):
        data = parser.parse_args()
        #foods是一个list类型，里面的元素是food_item的json
        foods = data['foods']
        for i in range(len(foods)):
            food = FoodDao.get_food_by_id(foods[i]['food_id'])
            #如果提交的food的信息数据库里面有相同id，则更新它
            if food != None:
                keys, values = service.get_keys_values(foods[i])
                FoodDao.update_food(foods[i]['food_id'], keys, values)
            #如果没有则创建
            else:
                FoodDao.add_food(foods[i]['food_id'], foods[i]['name'], foods[i]['price'],
                                foods[i]['food_type'], foods[i]['description'],
                                foods[i]['image'], foods[i]['available'], foods[i]['restaurant_id'])
        return {'URL': "/restaurants/%d/menu/%d"%(foods[0]['restaurant_id'], foods[0]['food_id'])}, 200

    #传入的food只有一个元素
    def delete(self):
        data = parser.parse_args()
        if FoodDao.get_food_by_id(data['foods']['food_id']) != None:
            FoodDao.del_food(data['foods']['food_id'])
            return 204
        else:
            return {"message": "The food is not in the menu"}, 400


#餐厅管理员操作餐厅菜单中的菜品
class admin_menu_food(Resource):
    def get(self):
        data = parser.parse_args()
        food = FoodDao.get_food_by_id(data['foods']['food_id'])
        if food == None:
            return {"message": "No such food exists in this menu"}, 400
        else:
            return {'foods': [food.__json__]}, 200

    def put(self):
        data = parser.parse_args()
        food = FoodDao.get_food_by_id(data['food_id'])
        if food == None:
            FoodDao.add_food(foods['food_id'], foods[i]['name'], foods[i]['price'],
                                foods[i]['food_type'], foods[i]['description'],
                                foods[i]['image'], foods[i]['available'], foods[i]['restaurant_id'])
        else:
            keys, values = service.get_keys_values(data)
            FoodDao.update_food(food, keys, values).


    def delete(self):
        data = parser.parse_args()
        if FoodDao.get_food_by_id(data['foods']['food_id']) != None:
            FoodDao.del_food(data['foods']['food_id'])
            return 204
        else:
            return {"message": "The food is not in the menu"}, 400
