from flask import Blueprint, request
from sqlalchemy.sql import func, text
from sqlalchemy.dialects.mysql import DATETIME
from werkzeug.security import generate_password_hash, check_password_hash

from utils import Result, JwtImpl, db

user = Blueprint("user", __name__)


# 用户
class TblUser(db.Model):
    __tablename__ = 'tbl_user'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), server_default="", nullable=False)
    _password = db.Column(db.String(256), server_default="", nullable=False, name="password")
    userrole = db.Column(db.String(128), server_default="")
    postname = db.Column(db.String(128), server_default="")
    # 昵称
    nick_name = db.Column(db.String(128), server_default="")
    create_by = db.Column(db.String(128), server_default="")
    update_by = db.Column(db.String(128), server_default="")
    login_ip = db.Column(db.String(20), server_default="")
    login_date = db.Column(DATETIME(fsp=3))
    # 留言
    remark = db.Column(db.String(128), server_default="")
    email = db.Column(db.String(128), server_default="")
    phone = db.Column(db.String(20), server_default="")
    sex = db.Column(db.CHAR(1), server_default="0")
    status = db.Column(db.CHAR(128), server_default="0")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    date = db.Column(DATETIME(fsp=3), server_default=func.now(3))

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}

    # 获取密码
    @property
    def password(self):
        return self._password

    # 设置密码
    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)  # 密码加密

    # 检查密码
    def chek_password(self, raw_password):
        result = check_password_hash(self._password, raw_password)
        return result


# 公司
class TblCorp(db.Model):
    __tablename__ = 'tbl_corp'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    corpname = db.Column(db.String(128), server_default="", nullable=False)
    create_by = db.Column(db.String(128), server_default="")
    update_by = db.Column(db.String(128), server_default="")
    status = db.Column(db.CHAR(128), server_default="0")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    date = db.Column(DATETIME(fsp=3), server_default=func.now(3))

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}


# 部门
class TblDept(db.Model):
    __tablename__ = 'tbl_dept'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    deptname = db.Column(db.String(128), server_default="", nullable=False)
    corpname = db.Column(db.String(128), server_default="")
    create_by = db.Column(db.String(128), server_default="")
    update_by = db.Column(db.String(128), server_default="")
    status = db.Column(db.CHAR(128), server_default="0")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    date = db.Column(DATETIME(fsp=3), server_default=func.now(3))

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}


# 职位
class TblPost(db.Model):
    __tablename__ = 'tbl_post'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    postname = db.Column(db.String(128), server_default="", nullable=False)
    deptname = db.Column(db.String(128), server_default="")
    corpname = db.Column(db.String(128), server_default="")
    create_by = db.Column(db.String(128), server_default="")
    update_by = db.Column(db.String(128), server_default="")
    status = db.Column(db.CHAR(128), server_default="0")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    date = db.Column(DATETIME(fsp=3), server_default=func.now(3))

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}


@user.route('/corp', methods=['GET', 'POST', 'PUT', 'DELETE'])
def CorpImpl():
    if request.method == 'GET':
        obj = TblCorp.query.filter().all()
        data_list = []
        for i in obj:
            data_list.append(i.to_dict())
        return Result.SUCCESS(data=data_list)
    if request.method == 'POST':
        corpname = request.json.get("corpname")
        obj = TblCorp.query.filter(TblCorp.corpname == corpname).first()
        if obj:
            return Result.ERROR(msg="当前公司已存在")
        obj = TblCorp(corpname=corpname)
        db.session.add(obj)
        db.session.flush()
        return Result.SUCCESS(msg="添加成功")
    elif request.method == 'PUT':
        obj = TblCorp.query.filter(TblCorp.uid == request.json.get("uid")).first()
        obj = request.json
        db.session.flush()
        return Result.SUCCESS(msg="修改成功")
    elif request.method == 'DELETE':
        obj = TblCorp.query.filter(TblCorp.uid == request.json.get("uid")).first()
        db.session.delete(obj)
        db.session.flush()
        return Result.SUCCESS(msg="删除成功")


@user.route('/dept', methods=['GET', 'POST', 'PUT', 'DELETE'])
def DeptImpl():
    if request.method == 'GET':
        obj = TblDept.query.filter().all()
        data_list = []
        for i in obj:
            data_list.append(i.to_dict())
        return Result.SUCCESS(data=data_list)
    elif request.method == 'POST':
        deptname = request.json.get("deptname")
        corpname = request.json.get("corpname")
        obj = TblDept.query.filter(TblDept.deptname == deptname).first()
        if obj:
            return Result.ERROR(msg="当前部门已存在")
        obj = TblDept(deptname=deptname, corpname=corpname)
        db.session.add(obj)
        db.session.flush()
        return Result.SUCCESS(msg="添加成功")
    elif request.method == 'PUT':
        obj = TblDept.query.filter(TblDept.uid == request.json.get("uid")).first()
        obj = request.json
        db.session.flush()
        return Result.SUCCESS(msg="修改成功")
    elif request.method == 'DELETE':
        obj = TblDept.query.filter(TblDept.uid == request.json.get("uid")).first()
        db.session.delete(obj)
        db.session.flush()
        return Result.SUCCESS(msg="删除成功")


@user.route('/post', methods=['GET', 'POST', 'PUT', 'DELETE'])
def PostImpl():
    if request.method == 'GET':
        obj = TblPost.query.filter().all()
        data_list = []
        for i in obj:
            data_list.append(i.to_dict())
        return Result.SUCCESS(data=data_list)
    elif request.method == 'POST':
        postname = request.json.get("postname")
        deptname = request.json.get("deptname")
        corpname = request.json.get("corpname")
        obj = TblPost.query.filter(TblPost.corpname == corpname).first()
        if obj:
            if obj.deptname == deptname:
                if obj.postname == postname:
                    pass
                else:
                    return Result.ERROR(msg="当前职位已存在")
            else:
                return Result.ERROR(msg="当前部门不存在")
        else:
            return Result.ERROR(msg="当前公司不存在")
        obj = TblPost(postname=postname, deptname=deptname)
        db.session.add(obj)
        db.session.flush()
        return Result.SUCCESS(msg="添加成功")
    elif request.method == 'PUT':
        obj = TblPost.query.filter(TblPost.uid == request.json.get("uid")).first()
        obj = request.json
        db.session.flush()
        return Result.SUCCESS(msg="修改成功")
    elif request.method == 'DELETE':
        obj = TblPost.query.filter(TblPost.uid == request.json.get("uid")).first()
        db.session.delete(obj)
        db.session.flush()
        return Result.SUCCESS(msg="删除成功")


@user.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getAll():
    if request.method == 'GET':
        obj = TblCorp.query.filter().all()
        data_list = []
        for i in obj:
            data_list.append(i.to_dict())
        return Result.SUCCESS(data=data_list)