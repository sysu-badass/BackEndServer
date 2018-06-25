# BackEndServer
This is the back end service for bad ass  scan-code-and-order-meal-system.
We will use python + flask to achieve it.

# 目录结构
.
├── app
│   ├── admin
│   │   ├── admin.py
│   │   └── __init__.py
│   ├── database
│   │   ├── dao_helper.py
│   │   ├── dao.py
│   │   ├── __init__.py
│   │   └── models.py
│   ├── __init__.py
│   ├── service
│   │   ├── __init__.py
│   │   └── sample_service.py
│   └── views
│       ├── __init__.py
│       └── sample_view.py
├── config.py
├── README.md
├── requirements.txt
├── run.py

# 目录及文件作用
* config.py: 项目配置文件
* run.py: 程序启动入口
* app: 项目包，app包的__init__.py用来加载程序配置，扩展和注册蓝图
  * admin: 权限管理包
  * database: 实现实体和实体的crud操作
     * models.py: 业务实体
     * dao.py: 实体的crud操作
     * dao_helper.py: crud操作的辅助模块
  * service: 业务包，实现对外提供的服务
  * views: restful api接口
      * sample_view.py: 演示view，实现登录，登出，edit

# 服务器运行
```sh
python run.py
```
# 登录
打开浏览器，访问（服务器ip：port/login）,比如在本地启动服务器，默认端口5000：  
访问127.0.0.1:5000/login

# 登出
打开浏览器，访问（服务器ip：port/logout）,比如在本地启动服务器，默认端口5000：  
访问127.0.0.1:5000/logout

# edit
打开浏览器，访问（服务器ip：port/edit/用户名）,比如在本地启动服务器，默认端口5000：  
访问127.0.0.1:5000/edit/ljx

# Reference
* 目录结构: https://blog.csdn.net/xingyunlost/article/details/77155584
