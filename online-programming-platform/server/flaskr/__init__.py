import os

from flask import Flask
from flask import request
from flask_cors import *
from .login import login 
from .comment import comment
from .signup import signup


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) 

    #注册蓝图
    app.register_blueprint(login,url_prefix='/login') 
    app.register_blueprint(comment,url_prefix='/comment') 
    app.register_blueprint(signup,url_prefix='/signup') 
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from . import db
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
 

    return app

