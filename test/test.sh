#!/bin/bash

# Test customer login 成功
curl -H "Content-Type: applicaton/json" -d '{"user_id": "3062", "username": "Jack", "user_password": "123456", "restaurant_id": 9527}' http://localhost:5000/users/login -X POST

# Test admin_join 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_id": 9527, "restaurant_admin_id": '123', "restaurant_admin_password": 1234, "restaurant_name": "Eorder", "restaurant_information": "小吃店"}' http://localhost:5000/restaurants/join -X POST

# Test admin_login 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_admin_id": "123", "restaurant_admin_password": 1234, "restaurant_id": 9527}' http://localhost:5000/restaurants/login -X POST

# Test admin_settings GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/settings -X GET

# Test admin_settings PUT 成功
curl -H "Content-Type: applicaton/json" -d '{"name": "The fourth canteen","information": "SYSU Canteen","address": "GuangZhou","phone_number": "88888888","open_time": "8:00-20:00","bulletin": "Stop Today","user_id": "123"}' http://localhost:5000/restaurants/9527/settings -X PUT

# Test admin_menu GET 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_id": 9527}' http://localhost:5000/restaurants/9527/menu -X GET

# Test admin_menu POST 成功
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"name": "豆腐","price": 10,"food_type": "素食","description": "美味","image": "/image/doufu.png","available": "True","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu -X POST

# Test admin_menu DELETE 成功
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"food_id": 1,"name": "豆腐","price": 10,"food_type": "素食","description": "美味","image": "/image/doufu.png","available": "True","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu -X DELETE

# Test admin_menu_food GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/menu/4 -X GET

# Test admin_menu_food PUT 成功
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"name": "臭豆腐","price": 10,"food_type": "素食","description": "恶心","image": "/image/doufu.png","available": "false","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu/4 -X PUT

# Test admin_menu_food DELETE 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/menu/4 -X DELETE

# Test admin_orders GET
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/orders -X GET

# Test admin_orders POST

# Test admin_orders DELETE

# Test admin_order GET

# Test admin_order POST

# Test admin_order DELETE
