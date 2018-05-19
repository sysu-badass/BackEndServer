from database.models import OrderHistory
from database.models import OrderHistoryItem
from database.models import Comment
from database.models import Restaurant
from database.models import Food
from database.models import Order
from database.models import OrderItem
from database.models import db
from database.dao_helper import DaoHelper
from datetime import datetime

class Dao:
    
    def get_order_history(self, id):
        order = OrderHistory.query.filter_by(id=id).first()
        return order
    
    def get_user_orders(self, user_id):
        orders = OrderHistory.query.filter_by(user_id=user_id).all()
        return orders
    
    def get_order_history_item(self, order_id):
        order_items = OrderHistoryItem.query \
                    .filter_by(order_history_id=order_id).all()
        return order_items

    def get_comment_by_id(self, comment_id):
        comment = Comment.query.filter_by(id=comment_id).first()
        return comment
    
    def get_user_comments(self, user_id):
        comments = Comment.query.filter_by(user_id=user_id).all()
        return comments
    
    def get_restaurant_comments(self, restaurant_id):
        comments = Comment.query.filter_by(restaurant_id=restaurant_id).all()
        return comments
    
    def get_restaurant_by_id(self, restaurant_id):
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
        return restaurant
    
    def get_restaurants(self, user_id):
        restaurants = Restaurant.query.filter_by(user_id=user_id).all()
        return restaurants

    def get_food_by_id(self, food_id):
        food = Food.query.filter_by(id=food_id).first()
        return food
    
    def get_foods(self, restaurant_id):
        foods = Food.query.filter_by(restaurant_id=restaurant_id).all()
        return foods
    
    def get_order(self, id):
        order = Order.query.filter_by(id=id).first()
        return order

    def get_restaurant_orders(self,restaurant_id):
        orders = Order.query.filter_by(restaurant_id=restaurant_id).all()
        return orders
    
    def get_order_item(self, order_id):
        order_items = OrderItem.query.filter_by(order_id=order_id).all()
        return order_items
    
    def add_order_history(self, date, desk_number, total_price,
                        restaurant_id, user_id):

        order = OrderHistory(date=date, desk_number=desk_number,
                        total_price=total_price, restaurant_id=restaurant_id,
                        user_id=user_id)

        flag = DaoHelper._add_comit(db, order)
        return flag
    
    def add_order_history_item(self, number, name, description,
                            image, price, order_id):

        order_item = OrderHistoryItem(number=number, name=name,
                                description=description,image=image,
                                price=price, order_id=order_id)

        flag = DaoHelper._add_comit(db, order_item)
        return flag
    
    def add_comment(self, name, star, text, image, restaurant_id, user_id):

        comment = Comment(name=name, star=star,
                    text=text, image=image,
                    restaurant_id=restaurant_id, user_id=user_id)

        flag = DaoHelper._add_comit(db, comment)
        return flag
    
    def add_restaurant(self, name, infomation, user_id):

        restaurant = Restaurant(name=name, infomation=infomation,
                            user_id=user_id)

        flag = DaoHelper._add_comit(db, restaurant)
        return flag
    
    def add_food(self, name, price, food_type,
            description, image, available, restaurant_id):

        food = Food(name=name, price=price, food_type=food_type,
                description=description, image=image, available=available,
                restaurant_id=restaurant_id)

        flag = DaoHelper._add_comit(db, food)
        return flag
    
    def add_order(self, date, desk_number, total_price, restaurant_id):

        order = Order(date=date, desk_number=desk_number,
                    total_price=total_price, restaurant_id=restaurant_id)

        flag = DaoHelper._add_comit(db, order)
        return flag
    
    def add_order_item(self, number, name, description, image, price, order_id):

        order_item = OrderItem(number=number, name=name,
                        description=description,image=image,
                        price=price, order_id=order_id)

        flag = DaoHelper._add_comit(db, order_item)
        return flag
    
    def update_restaurant(self, restaurant_id, key, value):
        restaurant = self.get_restaurant_by_id(restaurant_id)
        flag = DaoHelper._update_commit(db, restaurant, key, value)
        return flag
        
    def update_food(self, food_id, key, value):
        food = self.get_food_by_id(food_id)
        flag = DaoHelper._update_commit(db, food, key, value)
        return flag
    
    def del_order_history(self, order_id):
        order = self.get_order_history(order_id)
        flag = DaoHelper._del_commit(db, order)
        return flag

    def del_comment(self, comment_id):
        comment = self.get_comment_by_id(comment_id)
        flag = DaoHelper._del_commit(db, comment)
        return flag
    
    def del_restaurant(self, restaurant_id):
        restaurant = self.get_restaurant_by_id(restaurant_id)
        flag = DaoHelper._del_commit(db, restaurant)
        return flag
    
    def del_food(self, food_id):
        food = self.get_food_by_id(food_id)
        flag = DaoHelper._del_commit(db, food)
        return flag
    
    def del_order(self, order_id):
        order = self.get_order(order_id)
        flag = DaoHelper._del_commit(db, order)
        return flag
