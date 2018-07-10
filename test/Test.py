import os
import json

def test_url(command, exp_res, i):
	path = "res" + str(i) + '.json'
	not_ok = os.system(command + " > " + path)
	if not not_ok:
		with open(path) as f:
			res = json.load(f)
		return res == exp_res
if __name__ == '__main__':
	exp_res = [
		{
			"message": "This administrator already exists"
		},
		{
			"URL": "/restaurants/9527/menu"
		},
		
			204
		,
		{
			"name": "The fourth canteen",
		    "information": "SYSU Canteen",
		    "address": "GuangZhou",
		    "phone_number": "88888888",
		    "open_time": "8:00-20:00",
		    "bulletin": "Stop Today"
		},
		{
			"foods": [
		        {
		            "food_id": 9,
		            "image": "/image/doufu.png",
		            "description": "\u6076\u5fc3",
		            "available": False,
		            "food_type": "\u7d20\u98df",
		            "name": "\u81ed\u8c46\u8150",
		            "restaurant_id": 9527,
		            "price": 10.0
		        }
		    ]
		},
		{
			"message": "The food 1 is not in the menu"
		},
		{
			"URL": "/restaurants/9527/menu/1"
		},
		{
			"foods": [
		        {
		            "food_id": 9,
		            "image": "/image/doufu.png",
		            "description": "\u6076\u5fc3",
		            "available": False,
		            "food_type": "\u7d20\u98df",
		            "name": "\u81ed\u8c46\u8150",
		            "restaurant_id": 9527,
		            "price": 10.0
		        }
		    ]
		},
		{
			"message": "The food 1 is not in the menu"
		},
		{
			"URL": "/restaurants/9527/menu/1"
		},
		{
			"URL": "/restaurants/9527/orders/1"
		},
		{
			"orders":
		    [
		      {
		        'order_id': 1,
		        'desk_number': 2,
		        'total_price': 123.4,
		        'status': 'new',
		        'restaurant_id': 9527
		      }
		    ],
		    "order_items":
		    [
		      {
		        "number" : 2,
		        "name": "\u8c46\u8150",
		        "price": 10,
		        "description": "\u6076\u5fc3",
		        "image": "https://tse4-mm.cn.bing.net/th?id=OIP.0J7pU00aZiR-lzb_l-uCnQHaG_&pid=Api"
		      }
		    ]
		},
			204,
		{
			"URL": "/restaurants/9527/orders/1"
		},
		{
			"order_items":
		    [
		      {
		        "number" : 2,
		        "name": "\u8c46\u8150",
		        "price": 10,
		        "description": "\u6076\u5fc3",
		        "image": "https://tse4-mm.cn.bing.net/th?id=OIP.0J7pU00aZiR-lzb_l-uCnQHaG_&pid=Api"
		      }
		    ]
		},
			204,
		{
			"URL": "/restaurants/9527/orders/1"
		},
		{
			"order_items":
		    [
		      {
		        "number" : 2,
		        "name": "\u8c46\u8150",
		        "price": 10,
		        "description": "\u6076\u5fc3",
		        "image": "https://tse4-mm.cn.bing.net/th?id=OIP.0J7pU00aZiR-lzb_l-uCnQHaG_&pid=Api"
		      }
		    ]
		},
			204,
		{
			"message": "The food 1 is not in the order"
		},
		{
			"URL": "/restaurants/9527/menu/1"
		},
		{
			"foods": [
		        {
		            "food_id": 9,
		            "image": "/image/doufu.png",
		            "description": "\u6076\u5fc3",
		            "available": False,
		            "food_type": "\u7d20\u98df",
		            "name": "\u81ed\u8c46\u8150",
		            "restaurant_id": 9527,
		            "price": 10.0
		        }
		    ]
		},
		{
			"message": "The food 1 is not in the menu"
		},
		{
			"orders":
		    [
		      {
		        'order_id': 1,
		        'desk_number': 2,
		        'total_price': 123.4,
		        'status': 'new',
		        'restaurant_id': 9527
		      }
		    ],
		    "order_items":
		    [
		      {
		        "number" : 2,
		        "name": "\u8c46\u8150",
		        "price": 10,
		        "description": "\u6076\u5fc3",
		        "image": "https://tse4-mm.cn.bing.net/th?id=OIP.0J7pU00aZiR-lzb_l-uCnQHaG_&pid=Api"
		      }
		    ]
		},
			204,
		{
			"URL": "/restaurants/9527/orders/1"
		}
	]
	with open('Test.sh') as f:
		commands = f.readlines()
	for i in range(len(commands)):
		ok = test_url(commands[i].strip('\n'), exp_res[i], i)
		if ok:
			print("ok")
		else:
			print(str(i) + ": fail")

