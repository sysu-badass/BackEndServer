from flask import Flask
from passlib.hash import oracle10

#关于用户密码的存储，我打算将原始密码与用户账号用passlib.hash.oracle10的
#hash方法生成一串hash值，并将这串hash值作为用户密码存入到数据库中作为用户
#的密码，检验时将原始密码，hash值与账号检验即可

class User_service:
    #返回一串hash值
    @staticmethod
    def hash_password(password, account):
        return oracle10.hash(str`(password), user=str(account))

    #如果密码正确返回True
    @staticmethod
    def hash_password_verify(password, hash_password, account):
        return oracle10.verify(str(password), str(hash_password), user=str(account))


class Customer_service(User_service):
    pass

class Admin_service(User_service):
    pass
