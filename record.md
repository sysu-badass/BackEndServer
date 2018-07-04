* 顾客的id设置为string， 用户名可删去，其他类的id则还是integer
* 加个setting的url用于修改餐厅信息
* 餐厅登录是手机号与密码，顾客登录是string
* 订单的id与日期由后端生成，因此直接GET与POST都不返回id了
* 餐厅拒绝订单，发信号到顾客那里


## 尝试

* 要尝试一下将order_id作为None传入数据库中，看看数据库是否会自动赋值
