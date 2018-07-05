* 顾客的id设置为string， 用户名可删去，其他类的id则还是integer
* 加个setting的url用于修改餐厅信息
* 餐厅登录是手机号与密码，顾客登录是string
* 订单的id与日期由后端生成，因此直接GET与POST都不返回id了
* 餐厅拒绝订单，发信号到顾客那里


## 尝试

* 要尝试一下将order_id作为None传入数据库中，看看数据库是否会自动赋值
* 找到一个bug，是在/restaurant/settings那里的put函数，由于put的data中没有'id'key,而直接data['id']调用不存在的key是会报错的，后来用has_key('id')来进行判断，预计后面应该也要进行类似的尝试
* json传递的只接受integer与string类型,因此像food类型中的available属性不可以直接为True,只能先以字符串POST到服务端，再转为bool类型
* 与前端交流过后，餐厅管理员无论是更新还是添加都是会将完整的、写于API设计中的json数据结构POST到服务端，因此可以暂时不用写判断是否需要排除掉不存在的数据的代码
