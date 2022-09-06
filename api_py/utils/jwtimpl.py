import datetime

from flask import current_app
import jwt
from jwt import exceptions
from utils.result import Result


# 构造header
headers = {
    'typ': 'jwt',
    'alg': 'HS256'
}

SALT = 'a6gr2o0ffu4r2o0i3jr0ffu4r2o0'


class JwtImpl:

    @classmethod
    def create_token(cls, username, userrole):
        # 构造payload
        payload = {
            'username': username,
            'userrole': userrole,  # 自定义用户ID
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)  # 超时时间
        }
        result = jwt.encode(payload=payload, key=SALT, algorithm="HS256", headers=headers)\
            .encode('utf-8').decode('utf-8')
        return result

    @classmethod
    def verify_jwt(cls, token, secret=None):
        """
        检验jwt
        :param token: jwt
        :param secret: 密钥
        :return: dict: payload
        """
        if not secret:
            secret = current_app.config['JWT_SECRET']

        try:
            payload = jwt.decode(token.encode('utf-8'), secret, algorithms=['HS256'])
            return payload
        except exceptions.ExpiredSignatureError:  # 'token已失效'
            return Result.ERROR(msg='token已失效')
        except jwt.DecodeError:  # 'token认证失败'
            return Result.ERROR(msg='token认证失败')
        except jwt.InvalidTokenError:  # '非法的token'
            return Result.ERROR(msg='非法的token')
