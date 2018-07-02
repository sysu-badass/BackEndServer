#!/bin/bash

#Test customer login
curl -H "Content-Type: applicaton/json" -d '{"user_id": 3062, "username": "Jack", "user_password": "123456", "restaurant_id": 9527}' http://localhost:5000/users/login -X POST
