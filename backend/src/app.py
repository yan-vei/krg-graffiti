from flask import Flask
from flask_cors import CORS
from routes import images
from models.entity import Base, engine


def create_app():

	app = Flask(__name__)
	CORS(app)

	app.register_blueprint(images.images)

	Base.metadata.create_all(engine)
	return app
