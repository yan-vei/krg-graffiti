from flask import Flask
from flask_cors import CORS
from backend.src.models.entity import Base, engine
from backend.src.routes import images


def create_app():
	app = Flask(__name__)
	CORS(app)

	app.register_blueprint(images.images)

	Base.metadata.create_all(engine)
	return app