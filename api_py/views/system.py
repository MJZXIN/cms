import datetime

from flask import Blueprint, request, jsonify, g
from sqlalchemy import func, text
from sqlalchemy.dialects.mysql import DATETIME

from utils import Result, JwtImpl, db, TblDept, TblCorp, TblPost, TblUser, TblRole, has_roles

# from views.auth import login_required

system = Blueprint("system", __name__)


@system.route("/corp/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getCorp(page):
    pagination = TblCorp.query.filter().paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0
    }
    for i in posts:
        res["data_list"].append(i.to_dict())
    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@system.route("/corp", methods=['POST'])
@has_roles(["SYSTEM", "ADMIN"])
def addCorp():
    formData = request.json
    res = TblCorp.query.filter(TblCorp.corpname == formData.get("corpname")).first()
    if res:
        return Result.ERROR(msg="当前公司已存在")
    obj = TblCorp(corpname=formData.get("corpname"), city=formData.get("city"), address=formData.get("address"),
                  status=formData.get("status"), create_by=g.userinfo.get("username"))
    db.session.add(obj)
    db.session.flush()

    return Result.SUCCESS(msg="添加成功")


# @system.route("/user", methods=['POST'])
# @has_roles(["SYSTEM", "ADMIN"])
# def addUser():
#     demoList = ['USER', 'ADMIN', 'SYSTEM']
#     t = ":"
#     userrole = t.join(demoList)
#     print()
#     for i in ['USER']:
#         if i in demoList:
#             print("True")
#         else:
#             print("False")
#     return Result.SUCCESS(msg=t.join(demoList))


@system.route("/dept/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getCorpForDept(page):
    deptData = TblDept.query.filter().order_by(TblDept.corpname)
    pagination = deptData.group_by(TblDept.corpname).paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0,
        "corp_list": []
    }

    # # 缓存当前操作的公司名称
    # cur_corp = ""
    # #
    # data = []

    # # 遍历所有的部门信息
    # for i in posts:
    #
    #     # 判断当前行中数据是否为最新
    #     if i.corpname != cur_corp:
    #         cur_corp = i.corpname
    #         data.append({
    #             "uid": i.uid,
    #             "name": i.corpname,
    #             "create_by": i.create_by,
    #             "hasChildren": True,
    #             "children": []
    #         })
    #
    #     if data[len(data) - 1]["name"] == i.corpname:
    #         data[len(data) - 1]["children"].append({
    #             "uid": i.uid,
    #             "name": i.deptname,
    #             "create_by": i.create_by,
    #             "hasChildren": False,
    #             "children": []
    #         })
    for i in posts:
        res["data_list"].append({
            "uid": i.uid,
            "name": i.corpname,
            "status": i.status,
            "create_by": i.create_by,
            "hasChildren": True,
            "children": []
        })
        res["corp_list"].append(i.corpname)

    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@system.route("/dept")
@has_roles(["SYSTEM", "ADMIN"])
def getDeptByCorp():
    pagination = TblDept.query.filter(TblDept.corpname == request.args.get("corp")).all()
    res = []
    for i in pagination:
        res.append({
            "id": i.uid,
            "name": i.deptname,
            "status": i.status,
            "create_by": i.create_by,
            "hasChildren": False,
        })
    return Result.SUCCESS(data=res, msg="")


@system.route("/dept/corp")
@has_roles(["SYSTEM", "ADMIN"])
def getCorpList():
    pagination = TblDept.query.filter().group_by(TblDept.corpname).all()
    res = []
    for i in pagination:
        res.append(i.corpname)
    return Result.SUCCESS(data=res, msg="")


@system.route("/dept", methods=["POST"])
@has_roles(["SYSTEM", "ADMIN"])
def addDept():
    res = TblDept.query.filter(TblDept.corpname == request.json.get("corpname"),
                               TblDept.deptname == request.json.get("deptname")).first()
    if res:
        return Result.ERROR(msg="公司中已存在当前部门")
    obj = TblDept(corpname=request.json.get("corpname"), deptname=request.json.get("deptname"),
                  create_by=g.userinfo.get("username"),
                  status=request.json.get("status"))
    db.session.add(obj)
    db.session.flush()
    return Result.SUCCESS(msg="添加成功")


@system.route("/post/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getPost(page):
    pagination = TblPost.query.filter().paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0
    }
    for i in posts:
        res["data_list"].append(i.to_dict())
    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@system.route("/post", methods=["POST"])
@has_roles(["SYSTEM", "ADMIN"])
def addPost():
    res = TblPost.query.filter((TblPost.postcode == request.json.get("postcode") or
                                TblPost.postname == request.json.get("postname"))).first()
    if res:
        return Result.ERROR(msg="当前岗位已存在")
    obj = TblPost(postcode=request.json.get("postcode"), postname=request.json.get("postname"),
                  create_by=g.userinfo.get("username"),
                  status=request.json.get("status"))
    db.session.add(obj)
    db.session.flush()
    return Result.SUCCESS(msg="添加成功")


@system.route("/role/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getRole(page):
    pagination = TblRole.query.filter().paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0
    }
    for i in posts:
        res["data_list"].append(i.to_dict())
    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@system.route("/role", methods=["POST"])
@has_roles(["SYSTEM", "ADMIN"])
def addRole():
    res = TblRole.query.filter((TblRole.rolename == request.json.get("rolename") or
                                TblRole.rolecode == request.json.get("rolecode"))).first()
    if res:
        return Result.ERROR(msg="当前岗位已存在")
    obj = TblRole(rolename=request.json.get("rolename"), rolecode=request.json.get("rolecode"),
                  create_by=g.userinfo.get("username"),
                  status=request.json.get("status"))
    db.session.add(obj)
    db.session.flush()
    return Result.SUCCESS(msg="添加成功")


@system.route("/user/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getUser(page):
    pagination = TblUser.query.filter().paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0,
        "role_list": [],
        "dept_list": []
    }
    for i in posts:
        res["data_list"].append(i.to_dict())

    cur_corp = ""
    temp = TblDept.query.filter().order_by(TblDept.corpname).all()
    for i in temp:
        if i.corpname != cur_corp:
            cur_corp = i.corpname
            res["dept_list"].append({
                "value": i.corpname,
                "label": i.corpname,
                "children": [{
                    "label": i.deptname,
                    "value": i.deptname
                }]
            })
        else:
            res["dept_list"][len(res["dept_list"]) - 1]["children"].append({
                "label": i.deptname,
                "value": i.deptname
            })

    temp = TblRole.query.filter().order_by(TblRole.rolename).all()
    for i in temp:
        res["role_list"].append({
            "label": i.rolename,
            "value": i.rolecode
        })
    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@system.route("/user", methods=["POST"])
@has_roles(["SYSTEM", "ADMIN"])
def addUser():
    res = TblUser.query.filter(TblUser.username == request.json.get("username")).first()
    if res:
        return Result.ERROR(msg="当前用户已存在")
    role = ":".join(request.json.get("rolename"))
    dept = ":".join(request.json.get("deptname"))
    obj = TblUser(username=request.json.get("username"), password=request.json.get("password"), rolename=role,
                  deptname=dept, email=request.json.get("email"),
                  phone=request.json.get("phone"),
                  create_by=g.userinfo.get("username"),
                  status=request.json.get("status"))
    db.session.add(obj)
    db.session.flush()
    return Result.SUCCESS(msg="添加成功")
