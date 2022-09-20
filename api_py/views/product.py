from flask import Blueprint, request, g

from utils import Result, TblPart, TblWhsh, has_roles, TblProd, db, TblCorp

product = Blueprint("product", __name__)


@product.route("/part/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getPart(page):
    pagination = TblPart.query.filter().paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0,
        "whsh_list": []
    }

    whshDB = TblWhsh.query.filter().group_by(TblWhsh.corpname).all()
    for i in posts:
        res["data_list"].append(i.to_dict())

    cur_whsh = ""
    for whsh in whshDB:
        if cur_whsh != whsh.whshname:
            res["whsh_list"].append({
                "label": whsh.corpname,
                "value": whsh.corpname,
                "children": []
            })
        res["whsh_list"][len(res["whsh_list"]) - 1]["children"].append({
            "label": whsh.whshname,
            "value": whsh.whshname,
        })
    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@product.route("/part", methods=["POST"])
@has_roles(["SYSTEM", "ADMIN"])
def addPart():
    obj = TblPart(partname=request.json.get("partname"), part_spec=request.json.get("part_spec"),
                  part_type=request.json.get("part_type"), whshname=":".join(request.json.get("whshname")),
                  part_cost=request.json.get("part_cost"), create_by=g.userinfo.get("username"),
                  status=request.json.get("status"))
    db.session.add(obj)
    db.session.flush()
    return Result.SUCCESS(msg="添加成功")


@product.route("/prod/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getProd(page):
    pagination = TblProd.query.filter().paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0,
        "whsh_list": []
    }

    whshDB = TblWhsh.query.filter().group_by(TblWhsh.corpname).all()
    for i in posts:
        res["data_list"].append(i.to_dict())

    cur_whsh = ""
    for whsh in whshDB:
        if cur_whsh != whsh.whshname:
            res["whsh_list"].append({
                "label": whsh.corpname,
                "value": whsh.corpname,
                "children": []
            })
        res["whsh_list"][len(res["whsh_list"]) - 1]["children"].append({
            "label": whsh.whshname,
            "value": whsh.whshname,
        })
    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@product.route("/whsh/<int:page>")
@has_roles(["SYSTEM", "ADMIN"])
def getWarehouse(page):
    pagination = TblWhsh.query.filter().group_by(TblWhsh.corpname).paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    res = {
        "data_list": [],
        "total_page": 0,
        "corp_list": []
    }
    for i in posts:
        res["data_list"].append({
            "uid": i.uid,
            "name": i.corpname,
            "date": i.date,
            "hasChildren": True,
            "children": []
        })

    temp = TblCorp.query.filter().order_by(TblCorp.corpname).all()
    for i in temp:
        res["corp_list"].append(i.corpname)
    res["total_page"] = pagination.pages
    return Result.SUCCESS(data=res, msg="")


@product.route("/whsh")
@has_roles(["SYSTEM", "ADMIN"])
def getDeptByCorp():
    pagination = TblWhsh.query.filter(TblWhsh.corpname == request.args.get("corp")).all()
    res = []
    for i in pagination:
        res.append({
            "id": i.uid,
            "name": i.whshname,
            "address": i.address,
            "status": i.status,
            "create_by": i.create_by,
            "hasChildren": False,
        })
    return Result.SUCCESS(data=res, msg="")


@product.route("/whsh", methods=["POST"])
@has_roles(["SYSTEM", "ADMIN"])
def addWhsh():
    res = TblWhsh.query.filter(TblWhsh.corpname == request.json.get("corpname"),
                               TblWhsh.whshname == request.json.get("whshname")).first()
    if res:
        return Result.ERROR(msg="公司中已存在仓库")
    obj = TblWhsh(whshname=request.json.get("whshname"), corpname=request.json.get("corpname"),
                  address=request.json.get("address"),
                  create_by=g.userinfo.get("username"),
                  status=request.json.get("status"))
    db.session.add(obj)
    db.session.flush()
    return Result.SUCCESS(msg="添加成功")
