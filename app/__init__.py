# defini a inicialização da aplicação
# -*- coding: utf-8 -*-
#coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    # app = Flask(__name__)
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app) 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    migrate = Migrate(app,db)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .item import item as item_blueprint
    app.register_blueprint(item_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    return app


