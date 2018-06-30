from flask import Flask, current_app, request, session, redirect, url_for, abort
from flask_login import LoginManager, login_user, logout_user, \
     login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, \
     identity_changed
from flask_restful import reqparse, abort, Api, Resource

from app import login_manager
from app.database.dao import UserDao, OrderHistory, OrderHistoryItem, \
     Restaurant, Food, Order, OrderItem

from app.service.joey_service import service

from app.admin.admin import ModIdentityPermission
from app.admin.admin import AccessUrlPermission

api = Api()
