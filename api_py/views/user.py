from flask import Blueprint, request
from sqlalchemy.sql import func, text
from sqlalchemy.dialects.mysql import DATETIME
from werkzeug.security import generate_password_hash, check_password_hash

from utils import Result, JwtImpl, db, TblUser, has_roles

user = Blueprint("user", __name__)

@user.route('/<int:page>/<int:page_size>')
@has_roles(['SYSTEM', 'ADMIN', 'USER'])
def getUser(page, page_size):
    pagination = TblUser.query.paginate(page, per_page=page_size, error_out=False)
    posts = pagination.items
    data = {
        "data": [],
        "pages": 0
    }
    for i in posts:
        data['data'].append(i.to_dict())
    data['pages'] = pagination.pages
    return Result.SUCCESS(data=data)


