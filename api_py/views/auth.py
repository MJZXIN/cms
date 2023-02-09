import datetime
import json

from flask import Blueprint, request, session

from utils import Result, JwtImpl, db, TblUser, TblRoute

auth = Blueprint("auth", __name__)

routes_list = [
    {
        "path": "/",
        "name": "home",
        "root": True,
        "hideMenu": False,
        "roles": [
            "ADMIN",
            "SYSTEM",
            "USER"
        ],
        "meta": {
            "title": "首页",
            "icon": "Monitor"
        },
        "component": "../views/layout/layout.vue",
        "children": [{
            "path": "",
            "name": "overview",
            "root": False,
            "hideMenu": False,
            "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
            ],
            "meta": {
                "title": "看板",
                "icon": "Monitor"
            },
            "component": "../views/home/dashboard.vue",
            "children": []
        }]
    },
    {
        "path": "/system",
        "name": "系统管理",
        "root": True,
        "hideMenu": False,
        "roles": [
            "ADMIN",
            "SYSTEM",
            "USER"
        ],
        "meta": {
            "title": "系统管理",
            "icon": "Setting",
        },
        "component": "../views/layout/layout.vue",
        "children": [
            {
                "path": "user",
                "name": "用户设置",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ],
                "meta": {
                    "title": "用户管理",
                    "icon": "Memo"
                },
                "component": "../views/system/user.vue",
                "children": []
            },
            {
                "path": "role",
                "name": "角色设置",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM"
                ],
                "meta": {
                    "title": "角色管理",
                    "icon": "Memo"
                },
                "component": "../views/system/role.vue",
                "children": []
            }, {
                "path": "post",
                "name": "岗位管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM"
                ],
                "meta": {
                    "title": "岗位管理",
                    "icon": "Menu"
                },
                "component": "../views/system/post.vue",
                "children": []
            }, {
                "path": "dept",
                "name": "部门管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM"
                ],
                "meta": {
                    "title": "部门管理",
                    "icon": "Menu"
                },
                "component": "../views/system/dept.vue",
                "children": []
            }, {
                "path": "corp",
                "name": "公司管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "SYSTEM"
                ],
                "meta": {
                    "title": "公司管理",
                    "icon": "Menu"
                },
                "component": "../views/system/corp.vue",
                "children": []
            }, {
                "path": "menu",
                "name": "菜单管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ],
                "meta": {
                    "title": "菜单管理",
                    "icon": "Menu"
                },
                "component": "../views/system/menu.vue",
                "children": []
            },
            {
                "path": "dict",
                "name": "字典管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ],
                "meta": {
                    "title": "字典管理",
                    "icon": "Menu"
                },
                "component": "../views/system/dict.vue",
                "children": []
            },
            {
                "path": "config",
                "name": "参数设置",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ],
                "meta": {
                    "title": "参数设置",
                    "icon": "Menu"
                },
                "component": "../views/system/config.vue",
                "children": []
            },
            {
                "path": "setting",
                "name": "系统设置",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ],
                "meta": {
                    "title": "系统设置",
                    "icon": "Memo"
                },
                "component": "../views/setting/system.vue",
                "children": []
            }
        ]
    },
    {
        "path": "/master",
        "name": "主数据管理",
        "root": True,
        "hideMenu": False,
        "roles": [
            "ADMIN",
            "SYSTEM",
            "USER"
        ],
        "meta": {
            "title": "主数据管理",
            "icon": "SetUp"
        },
        "component": "../views/layout/layout.vue",
        "children": [
            {
                "path": "",
                "name": "产品管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ],
                "meta": {
                    "title": "物料管理",
                    "icon": "SetUp"
                },
                "component": "../views/product/product.vue",
                "children": []
            },
            {
                "path": "part",
                "name": "零件管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                ],
                "meta": {
                    "title": "零件管理",
                    "icon": "SetUp"
                },
                "component": "../views/product/part.vue",
                "children": []
            },
            {
                "path": "cost",
                "name": "成本管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                ],
                "meta": {
                    "title": "成本管理",
                    "icon": "Notebook"
                },
                "component": "../views/product/cost.vue",
                "children": []
            },
            {
                "path": "bom",
                "name": "BOM管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                ],
                "meta": {
                    "title": "BOM管理",
                    "icon": "Guide"
                },
                "component": "../views/product/bom.vue",
                "children": []
            },
            {
                "path": "warehouse",
                "name": "仓库管理",
                "root": False,
                "hideMenu": False,
                "roles": [
                    "ADMIN",
                    "SYSTEM",
                ],
                "meta": {
                    "title": "仓库管理",
                    "icon": "Guide"
                },
                "component": "../views/master/warehouse.vue",
                "children": []
            }
        ]
    },
    {
        "path": "/about",
        "name": "about",
        "root": True,
        "hideMenu": False,
        "roles": [
            "ADMIN",
            "SYSTEM",
            "USER"
        ],
        "meta": {
            "title": "关于",
            "icon": "Help"
        },
        "component": "../views/layout/layout.vue",
        "children": [{
            "path": "",
            "name": "关于",
            "root": False,
            "hideMenu": False,
            "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
            ],
            "meta": {
                "title": "关于",
                "icon": "Help"
            },
            "component": "../views/about/about.vue",
            "children": []
        }]
    },
    {
        "path": "/:catchAll(.*)",
        "name": "404",
        "root": True,
        "hideMenu": True,
        "roles": [
            "ADMIN",
            "SYSTEM",
            "USER"
        ],
        "meta": {
            "title": "404",
            "icon": "IconMenu"
        },
        "component": "../views/error/404.vue",
        "children": []
    }
]


@auth.route("/login", methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    res = TblUser.query.filter(TblUser.username == username).first()
    if res:
        # 校验密码
        if res.chek_password(raw_password=password):
            token = JwtImpl.create_token(res.username, res.rolelist)
            res.login_date = datetime.datetime.now()
            res.login_ip = request.remote_addr
            db.session.flush()
            userinfo = {"username": res.username, "rolelist": res.rolelist}

            # routes =
            # for route in routes_list:
            #     obj = TblRoute(path=route['path'], name=route['name'], root=str(route['root']),
            #                    hidemenu=str(route['hideMenu']), roles=':'.join(route['roles']),
            #                    title=route['meta']['title'], icon=route['meta']['icon'], component=route['component'])
            #     db.session.add(obj)
            #     for item in route['children']:
            #         obj = TblRoute(path=item['path'], rootpath=route['path'], name=item['name'], root=str(item['root']),
            #                        hidemenu=str(item['hideMenu']), roles=':'.join(item['roles']),
            #                        title=item['meta']['title'], icon=item['meta']['icon'], component=item['component'])
            #         db.session.add(obj)

            routes_list = []
            res = TblRoute.query.filter().all()
            for route in res:
                if route.root == 'True':
                    routes_list.append({
                        "path": route.path,
                        "name": route.name,
                        "hidemenu": route.hidemenu,
                        "roles": route.roles.split(':'),
                        "meta": {
                            "title": route.title,
                            "icon": route.icon
                        },
                        "component": route.component,
                        "children": []
                    })
                else:
                    routes_list[-1]['children'].append({
                        "path": route.path,
                        "name": route.name,
                        "hidemenu": route.hidemenu,
                        "roles": route.roles.split(':'),
                        "meta": {
                            "title": route.title,
                            "icon": route.icon
                        },
                        "component": route.component,
                        "children": []
                    })
            # print(routes_list)

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
    obj = TblUser(username=username, password=password)
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
        "rolelist": payload.get("rolelist")
    }, msg="已登录")


@auth.route("/logout")
def logout():
    return Result.SUCCESS(msg="退出登录")
