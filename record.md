* 顾客的id设置为string， 用户名可删去，其他类的id则还是integer
* 加个setting的url用于修改餐厅信息
* 餐厅登录是手机号与密码，顾客登录是string
* 订单的id与日期由后端生成，因此直接GET与POST都不返回id了
* 餐厅拒绝订单，发信号到顾客那里


## 尝试

1. 要尝试一下将order_id作为None传入数据库中，看看数据库是否会自动赋值
2. 找到一个bug，是在/restaurant/settings那里的put函数，由于put的data中没有'id'key,而直接data['id']调用不存在的key是会报错的，后来用has_key('id')来进行判断，预计后面应该也要进行类似的尝试
3. json传递的只接受integer与string类型,因此像food类型中的available属性不可以直接为True,只能先以字符串POST到服务端，再转为bool类型
4. 与前端交流过后，餐厅管理员无论是更新还是添加都是会将完整的、写于API设计中的json数据结构POST到服务端，因此可以暂时不用写判断是否需要排除掉不存在的数据的代码
5. DaoHelper.update_food()有问题
6. 在admin_orders中，尝试添加order时，order_item是否可以自动添加order的id
7. 在MySQL中调用语句select * from order;会说是SQL syntax error
8. 在admin_orders中，发现delete失败，感觉有可能要连相关order_item也要一起删去
9. 尝试在网址中添加中文

## 尝试结果
1. 虽然不是order类而是尝试food类，在/restaurant/menu中尝试向menu POST的数据中并没有food_id，但是数据库中仍然成功建立了数据库，不过也发现建立的id是从1、2、3等顺序开始往下排的，如果前面，如id为1的food被删除，那么数据库仍会继续递增id。总而言之，确定用户POST、Delete与GET的food、order、orderHistory是不同的，POST不用id，GET与Delete有id


5. 发现DaoHelper.update_food()其实每次更新的都是一个key与一个value，而原来的代码显示的是key是list，value也是list，修改后就可以了
6. 发现原来的代码append的是order_item类，但是我们只有初始的dictionary，所以还是要调用OrderItemDao来添加order_items
7. order在MySQL中时关键字所以要转义具体[参考链接](https://blog.csdn.net/andyzhaojianhui/article/details/49586555)
8. 猜想正确，需要先将所有的依赖删掉先
9. 不可以，是bad request
