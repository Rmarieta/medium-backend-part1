from flask import Flask
# from flask_cors import CORS

def create_app():

    app = Flask(__name__)
    # cors = CORS(app)

    from app.views.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app

