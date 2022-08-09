from flask import Flask
from flask_assets import Environment, Bundle
from app.views.index_view import index

def create_app():
    app = Flask(__name__)
    
    assets = Environment(app)
    css = Bundle("src/main.css", output="dist/main.css")
    assets.register("css", css)
    css.build()

    app.register_blueprint(index)

    return app