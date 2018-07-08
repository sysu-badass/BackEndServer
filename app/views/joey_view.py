from flask import Flask, current_app, request, session, redirect, url_for, abort
from flask_login import LoginManager, login_user, logout_user, \
     login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, \
     identity_changed, Permission, UserNeed
from flask_restful import reqparse, abort, Api, Resource

from app import login_manager
from app.database.dao import UserDao, OrderHistoryDao, OrderHistoryItemDao, \
     RestaurantDao, FoodDao, OrderDao, OrderItemDao

from app.service.joey_service import service

from app.admin.admin import ModIdentityPermission
from app.admin.admin import AccessUrlPermission
from app.admin.admin import ModRestaurantPermission
from app import db
from app.database.dao_helper import DaoHelper
import pdb
import datetime

'''
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
parser.add_argument('food_id')
parser.add_argument('name')
parser.add_argument('food_type')
parser.add_argument('available')
parser.add_argument('order_item_id')
parser.add_argument('order_id')
parser.add_argument('orders')
parser.add_argument('foods')
parser.add_argument('order_items')
'''

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

#顾客登录的话，如果数据库里没有相关账号密码，则创建一个
class Customer_login(Resource):
    def post(self):
        #data = parser.parse_args()
        data = request.get_json(force = True)
        #pdb.set_trace()
        customer = UserDao.get_user_by_id(data['user_id'])
        if customer != None:
            if service.hash_password_verify(data['user_password'], customer.password, customer.id):
                login_user(customer)
                identity_changed.send(current_app._get_current_object(),
                                    identity=Identity(customer.id))

                return {'URL': "/users/%d/%d/menu"%(int(customer.id), data['restaurant_id'])}, 200
            else:
                return {'message': 'login error'}, 400
        else:
            #加密密码，可用service.hash_password_verify(password, hash_password, account)认证
            password = service.hash_password(data['user_password'], data['user_id'])
            UserDao.add_user(data['user_id'], password)
            DaoHelper.commit(db)

            customer = UserDao.get_user_by_id(data['user_id'])
            login_user(customer)
            identity_changed.send(current_app._get_current_object(),
                                    identity=Identity(customer.id))
            return {'URL': "/users/%d/%d/menu"%(int(data['user_id']), data['restaurant_id'])}, 200

#顾客查看订单列表
class Customer_orders(Resource):
    @login_required
    def get(self, user_id, restaurant_id):

        identityPermission = Permission(UserNeed(user_id))
        if not identityPermission.can():
            abort(403)

        customer_orders = OrderHistoryDao.get_user_orders(user_id, int(restaurant_id))
        return {'orders': [customer_order.__json__() for customer_order in customer_orders]}, 200

#顾客查看订单
class Customer_order(Resource):
    @login_required
    def get(self, user_id, restaurant_id, order_id):
        identityPermission = Permission(UserNeed(user_id))
        if not identityPermission.can():
            abort(403)

        customer_order_items = OrderHistoryItemDao.get_order_history_items(int(order_id))
        return {'order_items': [customer_order_item.__json__() for customer_order_item in customer_order_items]}, 200

#顾客查看订单中的菜品的信息
class Customer_order_food(Resource):
    @login_required
    def get(self, user_id, restaurant_id, order_id, food_id):
        identityPermission = Permission(UserNeed(user_id))
        if not identityPermission.can():
            abort(403)

        customer_order_items = OrderHistoryItemDao.get_order_history_items(int(order_id))
        for customer_order_item in customer_order_items:
            food = FoodDao.get_food_by_name(customer_order_item.name)
            if (food != None) and (food.id == int(food_id)):
                return {'foods': [food.__json__()]}, 200
        return {'message': "No such food exists in this order"}, 400

#顾客查看菜单
class Customer_menu(Resource):
    def get(self, restaurant_id, user_id):
        foods = FoodDao.get_foods(restaurant_id)
        return {'foods': [food.__json__() for food in foods]}, 200

#顾客查看菜单中菜品的信息
class Customer_menu_food(Resource):
    def get(self, user_id, restaurant_id, food_id):
        #data = parser.parse_args()
        food = FoodDao.get_food_by_id(int(food_id))
        #pdb.set_trace()
        if food == None:
            return {"message": "No such food %d exists in this menu"%(int(food_id))}, 400
        else:
            return {'foods': [food.__json__()]}, 200


#返回支付方法对应的网站,这是一个json数组类型
class Customer_payment(Resource):
    def get(self, restaurant_id, user_id):
        return {"URL": ["example.com"]}, 200
    @login_required
    def post(self, restaurant_id, user_id):
        identityPermission = Permission(UserNeed(user_id))
        if not identityPermission.can():
            abort(403)

        #data = parser.parse_args()
        data = request.get_json(force = True)
        order = data['orders'][0]
        order_items = data['order_items']
        today = datetime.datetime.now()
        #将request里面的json key转化为数据库model的key
        '''
        for i in order_items:
            temp_item['id'] = i['order_history_item_id']
            temp_item['number'] = i['number']
            temp_item['name'] = i['name']
            temp_item['description'] = i['description']
            temp_item['image'] = i['image']
            temp_item['price'] = i['price']
            temp_item['order_history_id'] = i['order_history_id']
            items.append(temp_item.copy())
        order_items = items
        '''
        #用户自身的订单记录
        OrderHistoryDao.add_order_history(today, order['desk_number'], order['total_price'],
                                        order['restaurant_id'], order['user_id'], order_items)
        #同时要发送到餐厅的订单记录
        OrderDao.add_order(today, order['desk_number'],
                            order['total_price'], order['restaurant_id'],
                            order_items)
        DaoHelper.commit(db)
        return 204

#餐厅管理员注册
class admin_join(Resource):
    def post(self):
        #data = parser.parse_args()
        data = request.get_json(force = True)
        admin = UserDao.get_user_by_id(data['restaurant_admin_id'])
        restaurant = RestaurantDao.get_restaurant_by_id(data['restaurant_id'])
        #如果管理员已经存在于数据库，则返回400，不存在就添加到数据库
        if admin != None:
            return {"message": "This administrator already exists"}, 400
        password = service.hash_password(data['restaurant_admin_password'], data['restaurant_admin_id'])
        UserDao.add_user(data['restaurant_admin_id'], password)
        #如果餐厅的ID不存在，则创建一个
        if restaurant == None:
            RestaurantDao.add_restaurant(data['restaurant_id'], data['restaurant_admin_id'])
        else:
            #更新餐厅的资料
            key = ['id', 'name', 'information', 'user_id']
            value = [data['restaurant_id'], data['restaurant_name'], data['restaurant_information'], data['restaurant_admin_id']]
            RestaurantDao.update_restaurant(data['restaurant_id'], key, value)
        #将所有的修改从ORM添加到实体数据库中
        DaoHelper.commit(db)
        return {'URL': '/restaurants/%d/menu'%(data['restaurant_id'])}, 200

#餐厅管理员登录
class admin_login(Resource):
    def post(self):
        #data = parser.parse_args()
        data = request.get_json(force = True)
        admin = UserDao.get_user_by_id(data['restaurant_admin_id'])
        #管理员存在且密码验证正确，则返回餐厅的菜单界面
        if (admin != None) and (service.hash_password_verify(data['restaurant_admin_password'], admin.password, admin.id)):
            login_user(admin)
            identity_changed.send(current_app._get_current_object(),
                                    identity=Identity(admin.id))

            return {'URL': "/restaurants/%d/menu"%(data['restaurant_id'])}, 200
        return {'message': 'Login error'}, 400


#餐厅管理员管理餐厅设置信息
class admin_settings(Resource):
    @login_required
    def get(self, restaurant_id):
        print(type(restaurant_id))

        ownerPermission = ModRestaurantPermission(restaurant_id)
        print(ownerPermission.can())
        if not ownerPermission.can():
            abort(403)

        restaurant = RestaurantDao.get_restaurant_by_id(restaurant_id)
        return restaurant.__json__(), 200

    @login_required
    def put(self, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        data = request.get_json(force = True)
        #由于登录时会将餐厅的id POST到数据库中，所以一定可以得到restaurant
        restaurant = RestaurantDao.get_restaurant_by_id(restaurant_id)
        #用于update restaurant数据库的字典
        dict = {}
        #pdb.set_trace()
        for key, value in restaurant.__json__().items():
            #由于需要先登录才可以进行以下操作，所以可以确认restaurant_id是必定存在的
            if (key == 'id'):
                continue
            #当数据库中的数据是None时，无论data中对应的数据是否为None都更新
            if (value == None):
                dict[key] = data[key]
            #虽然数据库中的数据不是None，但是data中对应的数据存在，所以更新
            elif (data[key] != None):
                dict[key] = data[key]
            #数据库中的数据不是None，且data中对应的数据时None，则用回原来的数据
            else:
                dict[key] = value
        #keys, values = service.get_keys_values(dict)
        RestaurantDao.update_restaurant(restaurant_id, dict)
        DaoHelper.commit(db)
        return 204

#餐厅管理员操作餐厅订单列表
class admin_orders(Resource):
    @login_required
    def get(self, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        #pdb.set_trace()
        restaurant_orders = OrderDao.get_restaurant_orders(int(restaurant_id))
        array = [restaurant_order.__json__() for restaurant_order in restaurant_orders]
        return {'orders': array}, 200

    #一次可以创建一个order类，每次订单包含其中的order_item类
    #@merchantPermission.require()
    @login_required
    def post(self, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        #data = parser.parse_args()
        data = request.get_json(force = True)
        #orders是list类型的，里面的元素是orderItem
        order_items = data['order_items']
        order = data['orders'][0]
        #订单的日期，year-month-day hour-minute-second
        today = datetime.datetime.now()
        #转化成string形式
        OrderDao.add_order(today, order['desk_number'], order['total_price'],
                            order['status'], order['restaurant_id'], order_items)
        DaoHelper.commit(db)
        #获得刚刚添加的订单被数据库分配的id
        #pdb.set_trace()
        order_id = OrderDao.get_restaurant_orders(restaurant_id)[-1].id
        return {"URL": "/restaurants/%d/orders/%d"%(int(restaurant_id), order_id)}, 200

    @login_required
    def delete(self, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        #data = parser.parse_args()
        data = request.get_json(force = True)
        #pdb.set_trace()
        if OrderDao.get_order(data['order_id']) == None:
            return {"message": "No such order %d exists"%(data['order_id'])}, 400
        else:
            OrderDao.del_order(data['order_id'])
            DaoHelper.commit(db)
            return 204

#餐厅管理员操作餐厅订单
class admin_order(Resource):
    @login_required
    def get(self, order_id, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        order_items = OrderItemDao.get_order_items(order_id)
        return {'order_items': [order_item.__json__() for order_item in order_items]}, 200

    @login_required
    def put(self, restaurant_id, order_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        #data = parser.parse_args()
        data = request.get_json(force = True)
        order_items = data['order_items']
        order_item = None
        #先把我们当前URL的order id的order_item选出来
        #然后再从中选择出name相同的部分，不是None则更新，None则创建
        for i in range(len(order_items)):
            for exist_item in OrderItemDao.get_order_items(int(order_id)):
                if order_items[i]['name'] == exist_item.name:
                    order_item = exist_item
                    break
            #如果提交的order_item的信息数据库里面有相同id，则更新它
            if order_item != None:
                #keys, values = service.get_keys_values(order_items[i])
                OrderItemDao.update_order_item(order_item.id, order_items[i])
            #如果没有则创建
            else:
                OrderItemDao.add_order_item(order_items[i]['number'], order_items[i]['name'],
                                order_items[i]['description'], order_items[i]['image'],
                                order_items[i]['price'], int(order_id))
        DaoHelper.commit(db)
        return {"URL": "/restaurants/%d/orders/%d"%(int(restaurant_id), int(order_id))}, 200
    #只能传入一个参数
    @login_required
    def delete(self, order_id, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        if OrderDao.get_order(int(order_id)) != None:
            OrderDao.del_order(int(order_id))
            DaoHelper.commit(db)
            return 204
        else:
            return {"message": "The order %d is not in the order"%(int(order_id))}, 400

#餐厅管理员操作餐厅订单中的菜品
class admin_order_food(Resource):
    @login_required
    def get(self, restaurant_id, order_id, food_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        food = FoodDao.get_food_by_id(food_id)
        if food == None:
            return {"message": "The food %d doesn't exist"%(int(food_id))}, 400
        return {"URL": "/restaurants/%d/menu/%d"%(int(restaurant_id), int(food_id))}, 200

#餐厅管理员操作餐厅菜单列表
class admin_menu(Resource):
    @login_required
    def get(self, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        foods = FoodDao.get_foods(restaurant_id)
        return {'foods': [food.__json__() for food in foods]}, 200

    @login_required
    def post(self, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        #data = parser.parse_args()
        data = request.get_json(force = True)
        #foods是一个list类型，里面的元素是food_item的json
        foods = data['foods']
        for i in range(len(foods)):
            food = FoodDao.get_food_by_name(foods[i]['name'])
            #如果提交的food的信息数据库里面有相同id，则更新它
            #pdb.set_trace()
            if food != None:
                foods[i]['available'] = service.str2bool(foods[i]['available'])
                #keys, values = service.get_keys_values(foods[i])
                FoodDao.update_food(food.id, foods[i])
            #如果没有则创建
            else:
                FoodDao.add_food(foods[i]['name'], foods[i]['price'],
                                foods[i]['food_type'], foods[i]['description'],
                                foods[i]['image'], service.str2bool(foods[i]['available']), foods[i]['restaurant_id'])
        DaoHelper.commit(db)
        food = FoodDao.get_food_by_name(foods[i]['name'])
        return {'URL': "/restaurants/%d/menu/%d"%(food.restaurant_id, food.id)}, 200

    #传入的food只有一个元素
    @login_required
    def delete(self, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        #data = parser.parse_args()
        data = request.get_json(force = True)
        if FoodDao.get_food_by_id(data['foods'][0]['food_id']) != None:
            FoodDao.del_food(data['foods'][0]['food_id'])
            DaoHelper.commit(db)
            return 204
        else:
            return {"message": "The food %d is not in the menu"%(data['foods'][0]['food_id'])}, 400


#餐厅管理员操作餐厅菜单中的菜品
class admin_menu_food(Resource):
    @login_required
    def get(self, food_id, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        food = FoodDao.get_food_by_id(food_id)
        if food == None:
            return {"message": "No such food exists in this menu"}, 400
        else:
            return {'foods': [food.__json__()]}, 200

    @login_required
    def put(self, restaurant_id, food_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        #data = parser.parse_args()
        data = request.get_json(force = True)
        food = FoodDao.get_food_by_id(food_id)
        #pdb.set_trace()
        if food == None:
            #由于传进来的json是数组形式来存储数据的，所以需要index来检索
            food = data['foods'][0]
            FoodDao.add_food(food['name'], food['price'],
                                food['food_type'], food['description'],
                                food['image'], service.str2bool(food['available']), food['restaurant_id'])
            food_id = FoodDao.get_food_by_name(food['name']).id
        else:
            #food['available'] = service.str2bool(food['available'])
            #keys, values = service.get_keys_values(data['foods'][0])
            dict = data['foods'][0]
            dict['available'] = service.str2bool(dict['available'])
            FoodDao.update_food(int(food_id), dict)
        #pdb.set_trace()
        DaoHelper.commit(db)
        return {"URL": "/restaurants/%d/menu/%d"%(int(restaurant_id), int(food_id))}, 200

    @login_required
    def delete(self, food_id, restaurant_id):
        ownerPermission = ModRestaurantPermission(restaurant_id)
        if not ownerPermission.can():
            abort(403)

        if FoodDao.get_food_by_id(food_id) != None:
            FoodDao.del_food(food_id)
            DaoHelper.commit(db)
            return 204
        else:
            return {"message": "The food %d is not in the menu"%(food_id)}, 400
