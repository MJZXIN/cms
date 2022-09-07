import datetime

from flask import Blueprint, request, jsonify

from utils import Result, JwtImpl, db
from views.user import TblUser

menu = Blueprint("menu", __name__)


@menu.route("/menu")
def getMenu():
    data_list = [
        {
            "path": "/",
            "meta": {
                "title": "首页",
                "icon": "",
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ]
            },
            "component": "components/Layout/layout.vue",
            "children": [
                {
                    "path": "/",
                    "name": "dashboard",
                    "meta": {
                        "title": "看板",
                        "icon": "",
                        "roles": [
                            "ADMIN",
                            "SYSTEM",
                            "USER"
                        ]
                    }
                }
            ]
        }, {
            "path": "/login",
            "meta": {
                "title": "登录",
                "icon": "",
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ]
            },
            "component": "views/auth/login.vue",
            "children": []
        }, {
            "path": "/register",
            "meta": {
                "title": "注册",
                "icon": "",
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ]
            },
            "component": "views/auth/register.vue",
            "children": []
        }, {
            "path": "/404",
            "meta": {
                "title": "404",
                "icon": "",
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ]
            },
            "component": "views/error/404.vue",
            "children": []
        }, {
            "path": "/*",
            "meta": {
                "title": "404",
                "icon": "",
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ]
            },
            "component": "views/error/404.vue",
            "children": []
        }
    ]
    return Result.SUCCESS(data=data_list)
