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
    def add_user(username, password):
        usr = User(username=username, password=password)
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


class OrderHistoryDao:
    @staticmethod
    def get_order_history(id):
        order = OrderHistory.query.filter_by(id=id).first()
        return order

    @staticmethod
    def get_user_orders(user_id):
        orders = OrderHistory.query.filter_by(user_id=user_id).all()
        return orders

    @staticmethod
    def add_order_history(date, desk_number, total_price,
                        restaurant_id, user_id, order_history_items):
        order = OrderHistory(date=date, desk_number=desk_number,
                        total_price=total_price, restaurant_id=restaurant_id,
                        user_id=user_id)
        for item in order_history_items:
            order.order_history_items.append(item)
        db.session.add(order)

    @staticmethod
    def del_order_history(order_id):
        order = OrderHistoryDao.get_order_history(order_id)
        DaoHelper.delete(db, order)


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


class RestaurantDao:
    @staticmethod
    def add_restaurant(name, infomation, user_id):
        restaurant = Restaurant(name=name, infomation=infomation,
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
    def update_restaurant(restaurant_id, key, value):
        restaurant = RestaurantDao.get_restaurant_by_id(restaurant_id)
        DaoHelper.update(restaurant, key, value)

    @staticmethod
    def del_restaurant(restaurant_id):
        restaurant = RestaurantDao.get_restaurant_by_id(restaurant_id)
        DaoHelper.delete(db, restaurant)


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
    def get_foods(restaurant_id):
        foods = Food.query.filter_by(restaurant_id=restaurant_id).all()
        return foods

    @staticmethod
    def update_food(food_id, key, value):
        food = FoodDao.get_food_by_id(food_id)
        DaoHelper.update(food, key, value)

    @staticmethod
    def del_food(food_id):
        food = FoodDao.get_food_by_id(food_id)
        DaoHelper.delete(db, food)


class OrderDao:
    @staticmethod
    def add_order(date, desk_number, total_price, restaurant_id, order_items):
        order = Order(date=date, desk_number=desk_number,
                    total_price=total_price, restaurant_id=restaurant_id)
        for item in order_items:
            order.order_items.append(item)
        db.session.add(order)

    @staticmethod
    def get_order(id):
        order = Order.query.filter_by(id=id).first()
        return order

    @staticmethod
    def get_restaurant_orders(self,restaurant_id):
        orders = Order.query.filter_by(restaurant_id=restaurant_id).all()
        return orders

    @staticmethod
    def del_order(order_id):
        order = OrderDao.get_order(order_id)
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
