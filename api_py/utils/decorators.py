import functools

from flask import g
from utils.result import Result


def has_role(role: str):
    def login_required_decorators(func):
        @functools.wraps(func)
        def decorated_function(*args, **kws):
            # 需要在登录状态调用, 检查是否为有admin权限的用户登录，
            # 如果不是，返回错误码；
            # if g.user.user_name != 'admin':
            #     raise CustomFlaskErr(USER_MUST_HAS_ADMIN_PRIVILEGE, status_code=401)
            #
            # # 验证权限是否为 admin, 不是的话，返回401错误
            # if g.user.role_id != Permission.ADMIN:
            #     raise CustomFlaskErr(USER_MUST_HAS_ADMIN_PRIVILEGE, status_code=401)

            # return f(*args, **kws)
            if role is None:
                return func(*args, **kws)

            # 拿到所有的权限
            if role in g.userinfo["rolename"]:
                return func(*args, **kws)

            return Result.ERROR(code=403, msg="权限不足")

        return decorated_function

    return login_required_decorators


def has_roles(roleList: list):
    def login_required_decorators(func):
        @functools.wraps(func)
        def decorated_function(*args, **kws):
            # 需要在登录状态调用, 检查是否为有admin权限的用户登录，
            # 如果不是，返回错误码；
            # if g.user.user_name != 'admin':
            #     raise CustomFlaskErr(USER_MUST_HAS_ADMIN_PRIVILEGE, status_code=401)
            #
            # # 验证权限是否为 admin, 不是的话，返回401错误
            # if g.user.role_id != Permission.ADMIN:
            #     raise CustomFlaskErr(USER_MUST_HAS_ADMIN_PRIVILEGE, status_code=401)

            # return f(*args, **kws)
            if roleList is None:
                return func(*args, **kws)
            # 拿到所有的权限
            for role in roleList:
                # 判断用户权限是否在要求中
                if role in g.userinfo["rolename"]:
                    return func(*args, **kws)

            return Result.ERROR(code=403, msg="权限不足")

        return decorated_function

    return login_required_decorators

# # 定义登录装饰器，判断用户是否登录
# def decorator_login(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # # 判断session是否保存了用户名，保存了即该用户已登录
#         # name = session.get('name')
#         # if name:
#         #     return func(*args, *kwargs)
#         # else:
#         #     # 未登录重定向到登录页面
#         #     return redirect(url_for('test.login'))
#     return wrapper
