from rbac.models import User
from rbac.models import db

class OrderHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    desk_number = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref='order_histories')

class OrderHistoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(150))
    image = db.Column(db.String(45))
    price = db.Column(db.Float, nullable=False)

    order_history_id = db.Column(db.Integer,
        db.ForeignKey('order_history.id', ondelete='CASCADE'), nullable=False)
    order_history = db.relationship('OrderHistory', backref='order_history_items')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    star = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(150))
    image = db.Column(db.String(45))

    restaurant_id = db.Column(db.Integer,
        db.ForeignKey('restaurant.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    
    user = db.relationship('User', backref='comments')
    restaurant = db.relationship('Restaurant', backref='comments')

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    infomation = db.Column(db.String(150))

    user_id = db.Column(db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref='restaurants')

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Float, nullable=False)
    food_type = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(150))
    image = db.Column(db.String(45))
    available = db.Column(db.Boolean, nullable=False)

    restaurant_id = db.Column(db.Integer,
        db.ForeignKey('restaurant.id', ondelete='CASCADE'), nullable=False)
    restaurant = db.relationship('Restaurant', backref='foods')


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    desk_number = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer,
        db.ForeignKey('restaurant.id', ondelete='CASCADE'), nullable=False)
    restaurant = db.relationship('Restaurant', backref='orders')


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(150))
    image = db.Column(db.String(45))
    price = db.Column(db.Float, nullable=False)

    order_id = db.Column(db.Integer,
        db.ForeignKey('order.id', ondelete='CASCADE'), nullable=False)
    order = db.relationship('Order', backref='order_items')
