from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db


user_role = db.Table('user_role',
    db.Column('user_id', db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('role_id', db.Integer,
        db.ForeignKey('role.id', ondelete='CASCADE'), primary_key=True)
)

role_permission = db.Table('role_permission',
    db.Column('role_id', db.Integer,
       db.ForeignKey('role.id', ondelete='CASCADE'), primary_key=True),
    db.Column('permission_id', db.Integer, 
        db.ForeignKey('permission.id', ondelete='CASCADE'), primary_key=True)
)

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(45))
    image = db.Column(db.String(45))

    roles = db.relationship('Role', secondary='user_role',
                            backref = db.backref('users'))

    def __repr__(self):
        return '<User %r>' % self.username

class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(45), nullable=False, unique=True)

    def __repr__(self):
        return '<Role %r>' % self.rolename

class Permission(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False, unique=True)

    roles = db.relationship('Role', secondary='role_permission',
                            backref = db.backref('permissions'))
    
    def __repr__(self):
        return '<Permission %r>' % self.url

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
