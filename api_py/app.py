from flask import Flask
from views import *

app = Flask(__name__)

app.register_blueprint(auth)


@app.route('/')
def version():
    return 'CMS Version 0.1.0'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
