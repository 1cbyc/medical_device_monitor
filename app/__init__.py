# from flask import Flask
# from dotenv import load_dotenv
# import os
#
# load_dotenv() # will load the env var from .env file
#
# def create_app():
#     app = Flask(__name__)
#
#     from .routes import bp as main_bp
#     app.register_blueprint(main_bp)
#
#     return app
    # this above used to be here
    # from . import routes
    # app.register_blueprint(routes.bp)
    #
    # return app
    #
    # with app.app_context():
    #     from . import routes
    #     return app


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://localhost:5432/medical_device_monitor')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    db.init_app(app)
    migrate.init_app(app,db)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # print("Database URI:", os.getenv('SQLALCHEMY_DATABASE_URI'))
    # print("Track Modifications:", os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))

    return app
