from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
from sqlalchemy.dialects.mysql import DATETIME
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy(session_options={"autocommit": True})


# 角色
class TblRole(db.Model):
    __tablename__ = 'tbl_role'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    rolename = db.Column(db.String(128), server_default="", nullable=False)
    rolecode = db.Column(db.String(128), server_default="", nullable=False)
    create_by = db.Column(db.String(128), server_default="")
    status = db.Column(db.CHAR(1), server_default="1")
    _date = db.Column(DATETIME(fsp=3), server_default=func.now(3), name="date")

    @property
    def date(self):
        return self._date.strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}


# 用户
class TblUser(db.Model):
    __tablename__ = 'tbl_user'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), server_default="", nullable=False)
    _password = db.Column(db.String(256), server_default="", nullable=False, name="password")
    deptname = db.Column(db.String(128), server_default="")
    postname = db.Column(db.String(128), server_default="")
    rolename = db.Column(db.String(128), server_default="")
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
    status = db.Column(db.CHAR(1), server_default="1")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    _date = db.Column(DATETIME(fsp=3), server_default=func.now(3), name="date")

    @property
    def date(self):
        return self._date.strftime("%Y-%m-%d %H:%M:%S")

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


# 岗位
class TblPost(db.Model):
    __tablename__ = 'tbl_post'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    postname = db.Column(db.String(128), server_default="", nullable=False)
    postcode = db.Column(db.String(128), server_default="")
    create_by = db.Column(db.String(128), server_default="")
    update_by = db.Column(db.String(128), server_default="")
    status = db.Column(db.CHAR(1), server_default="1")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    _date = db.Column(DATETIME(fsp=3), server_default=func.now(3), name="date")

    @property
    def date(self):
        return self._date.strftime("%Y-%m-%d %H:%M:%S")

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
    status = db.Column(db.CHAR(1), server_default="1")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    _date = db.Column(DATETIME(fsp=3), server_default=func.now(3), name="date")

    @property
    def date(self):
        return self._date.strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}


# 公司
class TblCorp(db.Model):
    __tablename__ = 'tbl_corp'
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    corpname = db.Column(db.String(128), server_default="", nullable=False)
    city = db.Column(db.String(128), server_default="")
    address = db.Column(db.String(256), server_default="")
    create_by = db.Column(db.String(128), server_default="")
    update_by = db.Column(db.String(128), server_default="")
    status = db.Column(db.CHAR(1), server_default="1")
    del_flag = db.Column(db.CHAR(1), server_default=text('0'))
    _date = db.Column(DATETIME(fsp=3), server_default=func.now(3), name="date")

    @property
    def date(self):
        return self._date.strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}
