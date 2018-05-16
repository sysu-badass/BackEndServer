from server import db
from flask_sqlalchemy import SQLAlchemy


user_role = db.Table('user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

role_permission = db.Table('role_permission',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)

    roles = db.relationship('Role', secondary='user_role',
                            backref=db.backref('users'))


    def __repr__(self):
        return '<User %r>' % self.username


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False)

    roles = db.relationship('Role', secondary='role_permission',
                            backref=db.backref('permissions'))
    
    def __repr__(self):
        return '<Permission %r>' % self.url

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.rolename


