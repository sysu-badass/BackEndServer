from .models import User
from .models import Role
from .models import Permission
from .models import OrderHistory
from .models import OrderHistoryItem
from .models import Comment
from .models import Restaurant
from .models import Food
from .models import Order
from .models import OrderItem
from .dao_helper import DaoHelper
from datetime import datetime

from app import db


class UserDao:
    @staticmethod
    #添加id作为参数
    def add_user(id, password):
        usr = User(id=id, password=password)
        db.session.add(usr)

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def get_user(username):
        user = User.query.filter_by(username=username).first()
        return user

    @staticmethod
    def update_user(user_id, key, value):
        user = UserDao.get_user_by_id(user_id)
        DaoHelper.update(user, key, value)

    @staticmethod
    def del_user(user_id):
        user = UserDao.get_user_by_id(user_id)
        DaoHelper.delete(db, user)


class RoleDao:
    @staticmethod
    def add_role(rolename):
        role = Role(rolename=rolename)
        db.session.add(role)

    @staticmethod
    def get_role(rolename):
        role = Role.query.filter_by(rolename=rolename).first()
        return role


class PermissionDao:
    @staticmethod
    def add_permission(url):
        permission = Permission(url=url)
        db.session.add(permission)

    @staticmethod
    def get_permission(url):
        permission = Permission.query.filter_by(url=url).first()
        return permission

#需要添加 restaurant_id 来限制get_user_orders()
class OrderHistoryDao:
    @staticmethod
    def get_order_history(id):
        order = OrderHistory.query.filter_by(id=id).first()
        return order

    @staticmethod
    def get_user_orders(user_id, restaurant_id):
        orders = OrderHistory.query.filter_by(user_id=user_id, restaurant_id=restaurant_id).all()
        return orders

    @staticmethod
    def add_order_history(date, desk_number, total_price,
                        restaurant_id, user_id, order_history_items):
        order = OrderHistory(date=date, desk_number=desk_number,
                        total_price=total_price, restaurant_id=restaurant_id,
                        user_id=user_id)
        db.session.add(order)
        order_id = OrderHistoryDao.get_user_orders(user_id, restaurant_id)[-1].id
        for item in order_history_items:
            OrderHistoryItemDao.add_order_history_item(item['number'], item['name'],
                                        item['description'], item['image'],
                                        item['price'], order_id)



    @staticmethod
    def del_order_history(order_id):
        order = OrderHistoryDao.get_order_history(order_id)
        DaoHelper.delete(db, order)

#Create OrderHistoryItemDao
class OrderHistoryItemDao:
    @staticmethod
    def get_order_history_item(history_item_id):
        order_item = OrderHistoryItem.query.filter_by(id=history_item_id).first()
        return order_item

    @staticmethod
    def get_order_history_items(hitory_id):
        order_items = OrderHistoryItem.query.filter_by(order_history_id=hitory_id).all()
        return order_items

    @staticmethod
    def add_order_history_item(number, name,
                            description, image, price, order_history_id):
        order = OrderHistoryItem(number=number, name=name,
                        description=description, image=image,
                        price=price, order_history_id=order_history_id)
        db.session.add(order)

    @staticmethod
    def del_order_history_item(hitory_id, history_item_id):
        order = OrderHistoryDao.get_order_history_item(hitory_id, history_item_id)
        DaoHelper.delete(db, order)

    @staticmethod
    def update_order_history_item(order_history_item_id, dict):
        order_history_item = OrderHistoryItemDao.get_order_item(order_history_item_id)
        for key, value in dict.items():
            DaoHelper.update(order_history_item, key, value)


class CommentDao:
    @staticmethod
    def add_comment(name, star, text, image, restaurant_id, user_id):
        comment = Comment(name=name, star=star,
                    text=text, image=image,
                    restaurant_id=restaurant_id, user_id=user_id)
        db.session.add(comment)

    @staticmethod
    def get_comment_by_id(comment_id):
        comment = Comment.query.filter_by(id=comment_id).first()
        return comment

    @staticmethod
    def get_user_comments(user_id):
        comments = Comment.query.filter_by(user_id=user_id).all()
        return comments

    @staticmethod
    def get_restaurant_comments(restaurant_id):
        comments = Comment.query.filter_by(restaurant_id=restaurant_id).all()
        return comments

    @staticmethod
    def del_comment(comment_id):
        comment = CommentDao.get_comment_by_id(comment_id)
        DaoHelper.delete(db, comment)

#改变RestaurantDao的一些方法
class RestaurantDao:
    @staticmethod
    def add_restaurant(restaurant_id, user_id):
        restaurant = Restaurant(id=restaurant_id,
                            user_id=user_id)
        db.session.add(restaurant)

    @staticmethod
    def get_restaurant_by_id(restaurant_id):
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
        return restaurant

    @staticmethod
    def get_restaurants(user_id):
        restaurants = Restaurant.query.filter_by(user_id=user_id).all()
        return restaurants

    @staticmethod
    def update_restaurant(restaurant_id, dict):
        restaurant = RestaurantDao.get_restaurant_by_id(restaurant_id)
        for key, value in dict.items():
            DaoHelper.update(restaurant, key, value)

    @staticmethod
    def del_restaurant(restaurant_id):
        restaurant = RestaurantDao.get_restaurant_by_id(restaurant_id)
        DaoHelper.delete(db, restaurant)

#Add id as argument to add_food
class FoodDao:
    @staticmethod
    def add_food(name, price, food_type,
            description, image, available, restaurant_id):
        food = Food(name=name, price=price, food_type=food_type,
                description=description, image=image, available=available,
                restaurant_id=restaurant_id)
        db.session.add(food)

    @staticmethod
    def get_food_by_id(food_id):
        food = Food.query.filter_by(id=food_id).first()
        return food

    @staticmethod
    def get_food_by_name(food_name):
        food = Food.query.filter_by(name=food_name).first()
        return food

    @staticmethod
    def get_foods(restaurant_id):
        foods = Food.query.filter_by(restaurant_id=restaurant_id).all()
        return foods

    @staticmethod
    def update_food(food_id, dict):
        food = FoodDao.get_food_by_id(food_id)
        for key, value in dict.items():
            DaoHelper.update(food, key, value)

    @staticmethod
    def del_food(food_id):
        food = FoodDao.get_food_by_id(food_id)
        DaoHelper.delete(db, food)

#add id to add_order()
class OrderDao:
    @staticmethod
    def add_order(date, desk_number, total_price, restaurant_id, order_items):
        order = Order(date=date, desk_number=desk_number,
                    total_price=total_price, restaurant_id=restaurant_id)
        db.session.add(order)
        #获得最新的订单的id，因为它的id是递增的，所以最后一个是最新的
        order_id = OrderDao.get_restaurant_orders(restaurant_id)[-1].id
        #根据传进来的order_item数据创建order_item类
        for item in order_items:
            OrderItemDao.add_order_item(item['number'], item['name'],
                                        item['description'], item['image'],
                                        item['price'], order_id)


    @staticmethod
    def get_order(id):
        order = Order.query.filter_by(id=id).first()
        return order

    @staticmethod
    def get_restaurant_orders(restaurant_id):
        orders = Order.query.filter_by(restaurant_id=restaurant_id).all()
        return orders

    @staticmethod
    def del_order(order_id):
        order = OrderDao.get_order(order_id)
        #获得order中的相关的所有order_item
        order_items = OrderItemDao.get_order_items(order_id)
        #删除所有相关的order_item
        for order_item in order_items:
            OrderItemDao.del_order_item(order_item.id)
        DaoHelper.delete(db, order)

#Create OrderIrem class
class OrderItemDao:
    @staticmethod
    def get_order_item(order_item_id):
        order_item = OrderItem.query.filter_by(id=order_item_id).first()
        return order_item

    @staticmethod
    def get_order_item_by_name(order_item_name):
        order_item = OrderItem.query.filter_by(name=order_item_name).first()
        return order_item

    @staticmethod
    def get_order_items(order_id):
        order_items = OrderItem.query.filter_by(order_id=order_id).all()
        return order_items

    @staticmethod
    def add_order_item(number, name,
                            description, image, price, order__id):
        order = OrderItem(number=number, name=name,
                        description=description, image=image,
                        price=price, order_id=order__id)
        db.session.add(order)

    @staticmethod
    def update_order_item(order_item_id, dict):
        order_item = OrderItemDao.get_order_item(order_item_id)
        for key, value in dict.items():
            DaoHelper.update(order_item, key, value)

    @staticmethod
    def del_order_item(order_item_id):
        order = OrderItemDao.get_order_item(order_item_id)
        DaoHelper.delete(db, order)




















    # def get_order_item(order_id):
    #     order_items = OrderItem.query.filter_by(order_id=order_id).all()
    #     return order_items
















    # def add_perm_to_role(url, rolename):
    #     permission = self.get_permission(url)
    #     role = self.get_role(rolename)
    #     True
    #     if permission and role:
    #         role.permissions.append(permission)
    #         db.session.add(db, role)
    #     else:
    #         False

    # def add_role_to_user(rolename, username):
    #     user = self.get_user(username)
    #     role = self.get_role(rolename)
    #     True
    #     if user and role:
    #         user.roles.append(role)
    #         db.session.add(db, user)
    #     else:
    #         False
