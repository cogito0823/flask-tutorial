import os

from flask import Flask


def create_app(test_config=None):
    # 创建 app 并配置
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # 当不是测试模式，而实例配置（存在 config.py 中）又存在，则加载实例配置
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 加载传入的 test_config
        app.config.from_mapping(test_config)

    # 确定实例目录存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 一个简单的 hello 页面
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app
