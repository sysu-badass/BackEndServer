from flask import Flask

from app.database.models import User
from app.database.models import Role
from app.database.models import Permission
from app.database.models import OrderHistory
from app.database.models import OrderHistoryItem
from app.database.models import Comment
from app.database.models import Restaurant
from app.database.models import Food
from app.database.models import Order
from app.database.models import OrderItem
from app.database.dao_helper import DaoHelper
from datetime import datetime

from app import db
from passlib.hash import oracle10

#关于用户密码的存储，我打算将原始密码与用户账号用passlib.hash.oracle10的
#hash方法生成一串hash值，并将这串hash值作为用户密码存入到数据库中作为用户
#的密码，检验时将原始密码，hash值与账号检验即可

class service:
    #返回一串hash值
    @staticmethod
    def hash_password(password, account):
        return oracle10.hash(str(password), user=str(account))

    #如果密码正确返回True
    @staticmethod
    def hash_password_verify(password, hash_password, account):
        return oracle10.verify(str(password), str(hash_password), user=str(account))

    #获得 dictionary 中的 key list
    @staticmethod
    def get_keys_values(dict):
        keys = []
        values = []
        for key, value in dict.items():
            keys.append(key)
            values.append(value)
        return (keys, values)

    #将json数据中的true或者false字符串转成bool类型
    @staticmethod
    def str2bool(string):
        return string.upper() == 'true'.upper()
