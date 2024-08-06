from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
    #
    # with app.app_context():
    #     from . import routes
    #     return app
