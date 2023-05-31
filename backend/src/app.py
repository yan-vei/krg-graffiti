from flask import Flask
from flask_cors import CORS
from backend.src.routes import images

app = Flask(__name__)
CORS(app)

app.register_blueprint(images.images)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)