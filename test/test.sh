#!/bin/bash

#Test customer login
curl -H "Content-Type: applicaton/json" -d '{"user_id": "3062", "username": "Jack", "user_password": "123456", "restaurant_id": 9527}' http://localhost:5000/users/login -X POST

# Test admin_join
curl -H "Content-Type: applicaton/json" -d '{"restaurant_id": 9527, "restaurant_admin_id": '123', "restaurant_admin_password": 1234, "restaurant_name": "Eorder", "restaurant_information": "小吃店"}' http://localhost:5000/restaurants/join -X POST

# Test admin_login
curl -H "Content-Type: applicaton/json" -d '{"restaurant_admin_id": "123", "restaurant_admin_password": 1234, "restaurant_id": 9527}' http://localhost:5000/restaurants/login -X POST
