#!/bin/bash

# Test customer login 成功
curl -H "Content-Type: applicaton/json" -d '{"user_id": "3062", "username": "Jack", "user_password": "123456", "restaurant_id": 9527}' http://localhost:5000/users/login -X POST --cookie-jar cookie_file.txt

# Test customer_orders GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/users/3062/9527/orders -X GET --cookie cookie_file.txt

# Test customer_order GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/users/3062/9527/orders/2 -X GET --cookie cookie_file.txt

# Test customer_order_food GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/users/3062/9527/orders/2/6 -X GET --cookie cookie_file.txt

# Test customer menu GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/users/3062/9527/menu -X GET --cookie cookie_file.txt

# Test customer menu food GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/users/3062/9527/menu/6 -X GET --cookie cookie_file.txt

# Test customer payment GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/users/3062/9527/payment -X GET --cookie cookie_file.txt

# Test customer payment POST 成功
curl -H "Content-Type: applicaton/json" -d '{"orders": [{"desk_number": 2,"total_price": 123.4,"restaurant_id": 9527, "user_id": "3062"}], "order_items": [{"number" : 2,"name": "豆腐","price": 10,"description": "美味","image": "/image/doufu.png"}]}' http://localhost:5000/users/3062/9527/payment -X POST  --cookie cookie_file.txt

# Test admin_join 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_id": 9527, "restaurant_admin_id": '123', "restaurant_admin_password": 1234, "restaurant_name": "Eorder", "restaurant_information": "小吃店"}' http://localhost:5000/restaurants/join -X POST

# Test admin_login 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_admin_id": "123", "restaurant_admin_password": 1234, "restaurant_id": 9527}' http://localhost:5000/restaurants/login -X POST  --cookie-jar cookie_file.txt

# Test admin_settings GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/settings -X GET --cookie cookie_file.txt

# Test admin_settings PUT 成功
curl -H "Content-Type: applicaton/json" -d '{"name": "The fourth canteen","information": "SYSU Canteen","address": "GuangZhou","phone_number": "88888888","open_time": "8:00-20:00","bulletin": "Stop Today","user_id": "123"}' http://localhost:5000/restaurants/9527/settings -X PUT --cookie cookie_file.txt

# Test admin_menu GET 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_id": 9527}' http://localhost:5000/restaurants/9527/menu -X GET --cookie cookie_file.txt

# Test admin_menu POST 成功
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"name": "豆腐","price": 10,"food_type": "素食","description": "美味","image": "https://tse4-mm.cn.bing.net/th?id=OIP.0J7pU00aZiR-lzb_l-uCnQHaG_&pid=Api","available": "True","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu -X POST --cookie cookie_file.txt

# Test admin_menu DELETE 成功
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"food_id": 1,"name": "豆腐","price": 10,"food_type": "素食","description": "美味","image": "/image/doufu.png","available": "True","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu -X DELETE --cookie cookie_file.txt

# Test admin_menu_food GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/menu/4 -X GET --cookie cookie_file.txt

# Test admin_menu_food PUT 成功
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"name": "臭豆腐","price": 10,"food_type": "素食","description": "恶心","image": "/image/doufu.png","available": "false","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu/4 -X PUT --cookie cookie_file.txt

# Test admin_menu_food DELETE 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/menu/4 -X DELETE --cookie cookie_file.txt

# Test admin_orders GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/orders -X GET --cookie cookie_file.txt

# Test admin_orders POST 成功
curl -H "Content-Type: applicaton/json" -d '{"orders": [{"desk_number": 2,"total_price": 123.4,"restaurant_id": 9527}], "order_items": [{"number" : 2,"name": "豆腐","price": 10,"description": "美味","image": "/image/doufu.png"}]}' http://localhost:5000/restaurants/9527/orders -X POST --cookie cookie_file.txt

# Test admin_orders DELETE 成功
curl -H "Content-Type: applicaton/json" -d '{"order_id": 1}' http://localhost:5000/restaurants/9527/orders -X DELETE --cookie cookie_file.txt

# Test admin_order GET 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/orders/3 -X GET --cookie cookie_file.txt

# Test admin_order PUT 成功
curl -H "Content-Type: applicaton/json" -d '{"order_items": [{"number" : 20, "name": "臭豆腐", "price": 10, "description": "美味", "image": "/image/doufu.png"}, {"number" : 40,"name": "豆腐","price": 10,"description": "美味","image": "/image/doufu.png"}]}' http://localhost:5000/restaurants/9527/orders/4 -X PUT --cookie cookie_file.txt

# Test admin_order DELETE 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/orders/4 -X DELETE --cookie cookie_file.txt

# Test admin_order_food 成功
curl -H "Content-Type: applicaton/json" http://localhost:5000/restaurants/9527/orders/3/6 -X GET --cookie cookie_file.txt
