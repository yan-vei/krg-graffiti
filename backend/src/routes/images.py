from flask import Blueprint
from flask import make_response, request
from backend.src.utils import aws_helper


images = Blueprint("images", __name__)


@images.route("/api/v1/images/upload", methods=['POST'])
def upload_image_to_aws():

    image = request.files['image']

    try:
        image_url = aws_helper.upload_to_aws(image)
        return make_response({"image_url": image_url}, 200)
    except:
        return make_response({"error": "Image failed to upload to AWS."}, 500)


