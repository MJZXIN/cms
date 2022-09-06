import jwt
from flask import Flask, current_app, request
from flask_cors import CORS
import pymysql
from jwt import exceptions

import config
from views import *
from utils import Result, JwtImpl, SALT, db


app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(user, url_prefix="/api/user")

app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Festo:Festo4.0@127.0.0.1:3306/cms_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, supports_credentials=True)
pymysql.install_as_MySQLdb()
db.init_app(app)

# @app.errorhandler(Exception)
# def error_handler(e):
#     """
#     全局异常捕获，也相当于一个视图函数
#     """
#     return Result.ERROR(msg=str(e))


app.secret_key = 'a6gr2o0ffu4r2o0i3jr0ffu4r2o0'
app.config['JSON_AS_ASCII'] = False
app.config['JWT_SECRET'] = 'a6gr2o0ffu4r2o0i3jr0ffu4r2o0'


# # 跨域支持
# def after_request(resp):
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp
#
#
# app.after_request(after_request)


@app.before_request
def jwt_authentication():
    """
        1.获取请求头Authorization中的token
        2.判断是否以 Bearer开头
        3.使用jwt模块进行校验
        4.判断校验结果,成功就提取token中的载荷信息,赋值给g对象保存
        """
    auth = request.headers.get('Authorization')
    print(request.path)
    whitelist = ["/api", "/api/login", "/api/reg", "/api/adb"]
    index = 0
    for i in whitelist:
        if request.path == i:
            index = 1
            break
    if index == 0:
        if auth:
            if auth.startswith('Bearer '):
                "提取token 0-6 被Bearer和空格占用 取下标7以后的所有字符"
                token = auth[7:]
            else:
                token = auth
            "校验token"
            try:
                "判断token的校验结果"
                payload = jwt.decode(token, SALT, algorithms=['HS256'])
                if payload.get('userrole') == 'SYSTEM':
                    pass
                elif payload.get('userrole') == 'ADMIN' and request.path.startswith('/api/user'):
                    pass
                elif payload.get('userrole') == 'USER' and request.path.startswith('/api/auth'):
                    pass
                else:
                    return Result.ERROR(code=403, msg='无权限访问')
            except exceptions.ExpiredSignatureError:  # 'token已失效'
                return Result.ERROR(msg='token已失效')
            except jwt.DecodeError:  # 'token认证失败'
                return Result.ERROR(msg='token认证失败')
            except jwt.InvalidTokenError:  # '非法的token'
                return Result.ERROR(msg='非法的token')
        else:
            return Result.ERROR(msg='无身份信息')


@app.route('/api')
def version():
    return 'CMS Version 0.1.0'


@app.route('/api/adb')
def adb():
    db.create_all()
    return "Done"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
