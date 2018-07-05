#!/bin/bash

#Test customer login 成功
curl -H "Content-Type: applicaton/json" -d '{"user_id": "3062", "username": "Jack", "user_password": "123456", "restaurant_id": 9527}' http://localhost:5000/users/login -X POST

# Test admin_join 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_id": 9527, "restaurant_admin_id": '123', "restaurant_admin_password": 1234, "restaurant_name": "Eorder", "restaurant_information": "小吃店"}' http://localhost:5000/restaurants/join -X POST

# Test admin_login 成功
curl -H "Content-Type: applicaton/json" -d '{"restaurant_admin_id": "123", "restaurant_admin_password": 1234, "restaurant_id": 9527}' http://localhost:5000/restaurants/login -X POST

# Test admin_settings 失败
curl -H "Content-Type: applicaton/json" -d '{"name": "The fourth canteen","information": "SYSU Canteen","address": "GuangZhou","phone_number": "88888888","open_time": "8:00-20:00","bulletin": "Stop Today","user_id": "123"}' http://localhost:5000/restaurants/9527/settings -X PUT

#Test admin_menu GET
curl -H "Content-Type: applicaton/json" -d '{"restaurant_id": 9527}' http://localhost:5000/restaurants/9527/menu -X GET

#Test admin_menu POST
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"name": "豆腐","price": 10,"food_type": "素食","description": "美味","image": "/image/doufu.png","available": "True","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu -X POST

#Test admin_menu DELETE
curl -H "Content-Type: applicaton/json" -d '{"foods": [{"food_id": 1,"name": "豆腐","price": 10,"food_type": "素食","description": "美味","image": "/image/doufu.png","available": "True","restaurant_id": 9527}]}' http://localhost:5000/restaurants/9527/menu -X DELETE
