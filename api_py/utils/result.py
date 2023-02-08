from flask import jsonify


class Result:

    def __int__(self):
        self.code = 0
        self.data = {}
        self.msg = ''

    @classmethod
    def SUCCESS(cls, msg=''):
        return jsonify({
            "code": 200,
            "data": {},
            "msg": msg
        })

    @classmethod
    def SUCCESS(cls, data={}):
        return jsonify({
            "code": 200,
            "data": data,
            "msg": ''
        })

    @classmethod
    def SUCCESS(cls, code=200, data={}, msg=''):
        return jsonify({
            "code": code,
            "data": data,
            "msg": msg
        })

    @classmethod
    def ERROR(cls, code=0, data={}, msg='500 服务器错误'):
        return jsonify({
            "code": code,
            "data": data,
            "msg": msg
        })
