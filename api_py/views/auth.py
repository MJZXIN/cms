import datetime

from flask import Blueprint, request

from utils import Result, JwtImpl, db
from views.user import TblUser

auth = Blueprint("auth", __name__)

routes_list = [
    {
        "path": "/",
        "name": "home",
        "root": True,
        "hidden": False,
        "meta": {
            "title": "首页",
            "icon": "Monitor",
            "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
            ]
        },
        "component": "../views/layout/layout.vue",
        "children": [{
            "path": "",
            "name": "overview",
            "root": False,
            "hidden": False,
            "meta": {
                "title": "看板",
                "icon": "Monitor",
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ]
            },
            "component": "../views/home/dashboard.vue",
            "children": []
        }]
    },
    {
        "path": "/system",
        "name": "系统管理",
        "root": True,
        "hidden": False,
        "meta": {
            "title": "系统管理",
            "icon": "Setting",
            "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
            ]
        },
        "component": "../views/layout/layout.vue",
        "children": [
            {
                "path": "user",
                "name": "用户设置",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "用户管理",
                    "icon": "Memo",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                        "USER"
                    ]
                },
                "component": "../views/system/user.vue",
                "children": []
            },
            {
                "path": "role",
                "name": "角色设置",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "角色管理",
                    "icon": "Memo",
                    "roles": [
                        "ADMIN",
                        "SYSTEM"
                    ]
                },
                "component": "../views/system/role.vue",
                "children": []
            }, {
                "path": "post",
                "name": "岗位管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "岗位管理",
                    "icon": "Menu",
                    "roles": [
                        "ADMIN",
                        "SYSTEM"
                    ]
                },
                "component": "../views/system/post.vue",
                "children": []
            }, {
                "path": "dept",
                "name": "部门管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "部门管理",
                    "icon": "Menu",
                    "roles": [
                        "ADMIN",
                        "SYSTEM"
                    ]
                },
                "component": "../views/system/dept.vue",
                "children": []
            }, {
                "path": "corp",
                "name": "公司管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "公司管理",
                    "icon": "Menu",
                    "roles": [
                        "SYSTEM"
                    ]
                },
                "component": "../views/system/corp.vue",
                "children": []
            }, {
                "path": "menu",
                "name": "菜单管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "菜单管理",
                    "icon": "Menu",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                        "USER"
                    ]
                },
                "component": "../views/system/menu.vue",
                "children": []
            },
            {
                "path": "dict",
                "name": "字典管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "字典管理",
                    "icon": "Menu",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                        "USER"
                    ]
                },
                "component": "../views/system/dict.vue",
                "children": []
            },
            {
                "path": "config",
                "name": "参数设置",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "参数设置",
                    "icon": "Menu",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                        "USER"
                    ]
                },
                "component": "../views/system/config.vue",
                "children": []
            },
            {
                "path": "setting",
                "name": "系统设置",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "系统设置",
                    "icon": "Memo",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                        "USER"
                    ]
                },
                "component": "../views/setting/system.vue",
                "children": []
            }
        ]
    },
    {
        "path": "/product",
        "name": "产品管理",
        "root": True,

        "hidden": False,
        "meta": {
            "title": "产品管理",
            "icon": "SetUp",
            "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
            ]
        },
        "component": "../views/layout/layout.vue",
        "children": [
            {
                "path": "",
                "name": "产品管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "产品管理",
                    "icon": "SetUp",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                        "USER"
                    ]
                },
                "component": "../views/product/product.vue",
                "children": []
            },
            {
                "path": "part",
                "name": "零件管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "零件管理",
                    "icon": "SetUp",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                        "USER"
                    ]
                },
                "component": "../views/product/part.vue",
                "children": []
            },
            {
                "path": "cost",
                "name": "成本管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "成本管理",
                    "icon": "Notebook",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                    ]
                },
                "component": "../views/product/cost.vue",
                "children": []
            },
            {
                "path": "bom",
                "name": "BOM管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "BOM管理",
                    "icon": "Guide",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                    ]
                },
                "component": "../views/product/bom.vue",
                "children": []
            },
            {
                "path": "warehouse",
                "name": "仓库管理",
                "root": False,
                "hidden": False,
                "meta": {
                    "title": "仓库管理",
                    "icon": "Guide",
                    "roles": [
                        "ADMIN",
                        "SYSTEM",
                    ]
                },
                "component": "../views/product/warehouse.vue",
                "children": []
            }
        ]
    },
    {
        "path": "/about",
        "name": "about",
        "root": True,
        "hidden": False,
        "meta": {
            "title": "关于",
            "icon": "Help",
            "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
            ]
        },
        "component": "../views/layout/layout.vue",
        "children": [{
            "path": "",
            "name": "关于",
            "root": False,
            "hidden": False,
            "meta": {
                "title": "关于",
                "icon": "Help",
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ]
            },
            "component": "../views/about/about.vue",
            "children": []
        }]
    },
    {
        "path": "/:catchAll(.*)",
        "name": "404",
        "root": True,
        "hidden": True,
        "meta": {
            "title": "404",
            "icon": "IconMenu",
            "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
            ]
        },
        "component": "../views/error/404.vue",
        "children": []
    }
]


@auth.route("/login", methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    obj = TblUser.query.filter(TblUser.username == username).first()
    if obj:
        # 校验密码
        if obj.chek_password(raw_password=password):
            token = JwtImpl.create_token(obj.username, obj.rolename)
            obj.login_date = datetime.datetime.now()
            obj.login_ip = request.remote_addr
            db.session.flush()
            userinfo = {"username": obj.username, "rolename": obj.rolename.split(':')}
            # routes =
            return Result.SUCCESS(data={"token": token, "userinfo": userinfo, "routes": routes_list}, msg="登录成功")
        else:
            return Result.ERROR(msg="账号或密码错误")
    else:
        return Result.ERROR(msg="账号或密码错误")


@auth.route("/reg", methods=['POST'])
def reg():
    username = request.json.get("username")
    password = request.json.get("password")
    obj = TblUser.query.filter(TblUser.username == username).first()
    if obj:
        return Result.ERROR(msg="用户名已存在")
    obj = TblUser(username=username, password=password, rolename='USER')
    db.session.add(obj)
    db.session.flush()
    return Result.SUCCESS(msg="注册成功")


@auth.route("/auth")
def getInfo():
    token = request.headers['Authorization']
    if token.startswith('Bearer '):
        payload = JwtImpl.verify_jwt(token[7:])
    else:
        payload = JwtImpl.verify_jwt(token)

    return Result.SUCCESS(data={
        "username": payload.get("username"),
        "userrole": payload.get("userrole")
    }, msg="已登录")


@auth.route("/logout")
def logout():
    return Result.SUCCESS(msg="退出登录")
