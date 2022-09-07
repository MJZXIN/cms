import datetime

from flask import Blueprint, request, jsonify

from utils import Result, JwtImpl, db
from views.user import TblUser

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    obj = TblUser.query.filter(TblUser.username == username).first()
    if obj:
        # 校验密码
        if obj.chek_password(raw_password=password):
            token = JwtImpl.create_token(obj.username, obj.userrole)
            obj.login_date = datetime.datetime.now()
            obj.login_ip = request.remote_addr
            db.session.flush()
            return Result.SUCCESS(data={"token": token}, msg="登录成功")
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
    obj = TblUser(username=username, password=password, userrole='USER')
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
