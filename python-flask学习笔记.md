## python与flask的学习笔记

[toc]

### Flask

+ 首先若是在virtualenv中建立project，首先需要建立虚拟环境先，使用 virtualenv 命令在project文件夹中创建 Python 虚拟环境。这个命令只有一个必需的参数,即虚拟环境的名字。创建虚拟环境后,当前文件夹中会出现一个子文件夹,名字就是上述命令中指定的参数,与虚拟环境相关的文件都保存在这个子文件夹中。按照惯例,一般虚拟环境会被命名为venv,如**virtualenv venv**就可以创建虚拟环境了。 **(p26)**
+ Linux环境下可以通过**source venv/bin/activate**启动虚拟环境，并通过**deactivate**关闭虚拟环境。
+ 要运行Flask程序，需要以下命令，在Linux环境下，我们需要告诉系统Flask app是哪一个文件。先**export FLASK_APP = main.py**，再**flask run**。这里的main.py文件指的是我们的程序实例，里面有视图函数以及路由等信息。
+ 若想进入debug模式，需要 **app.run(debug=True)** 在app.run()函数里面添加参数debug，然后需要命令**export FLASK_DEBUG=1**，之后在运行命令 **flask run** 即可


### python
* 有关python的类的介绍 https://docs.python.org/3/tutorial/classes.html 主要有关其中的namespace and scope
* python 中immutable basic types 有numbers, strings, tuples，它们都是不可变的。
* 在python类中，\__str\__() and \__repr\__()的差别参考网址 https://stackoverflow.com/questions/1436703/difference-between-str-and-repr


### Python Passlib
[官方网站](https://passlib.readthedocs.io)
这个库主要用来将用户密码转化为hash值以保护用户隐私。
Example:
```python
from passlib.hash import oracle10
from passlib.hash import pbkdf2_sha256

password = “1234”
user="joey"
#password_hash将会生成一串hash值
password_hash = pbkdf2_sha256.hash(password)
#验证密码与hash值是否对应
pbkdf2_sha256.verify(password, password_hash) #True
pbkdf2_sha256.verify("password", password_hash) #False
#我打算将原始密码生成hash值，再将hash值作为密码存入数据库
#并且验证密码需要与账号对应，减少hash冲突的情况
hash = oracle10.hash(password_hash, user="admin")
#验证password_hash与user admin 是否对应
oracle10.verify(password_hash, hash, user="admin") #True
oracle10.verify(password_hash, hash, user="joey") #False
```

### Flask-login
[官方网站](https://flask-login.readthedocs.io/en/latest/)

### Flask-Restful
[官方网站](https://flask-restful.readthedocs.io/en/latest/)
* api.add_resoure()方法可以让一个资源拥有多个URL，例如 **api.add_resource(HelloWorld,'/','/hello')** ，那么在'/'与'/hello'URL都会是HelloWorld resource
* reqparse.RequestParser.parse_args()可以获得 request 里面的数据，而且时以dictionary的形式来读取的。

### Flask-jwt-extended
[官方网站](https://flask-jwt-extended.readthedocs.io/en/latest)

### Flask-SQLAlchemy
[官方网站](http://www.pythondoc.com/flask-sqlalchemy/index.html)
