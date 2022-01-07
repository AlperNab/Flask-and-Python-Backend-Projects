from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from HiringCars.config import Config




#db = MySQL()
db = SQLAlchemy()
def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///site.db'
    db.init_app(app)


    from HiringCars.actions.routes import action
    from HiringCars.errors.handlers import errors


    app.register_blueprint(action)
    app.register_blueprint(errors)

    return app
