from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() # will load the env var from .env file

def create_app():
    app = Flask(__name__)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
    #
    # from . import routes
    # app.register_blueprint(routes.bp)
    #
    # return app
    #
    # with app.app_context():
    #     from . import routes
    #     return app
