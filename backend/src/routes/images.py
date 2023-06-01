from flask import Blueprint, jsonify
from flask import make_response, request
from backend.src.utils import aws_helper
from backend.src.crud import graffiti


images = Blueprint("images", __name__)


@images.route("/api/v1/images/upload", methods=['POST'])
def upload_image_to_aws():
    graffiti_data = request.form.to_dict()
    image = request.files['image']

    try:
        image_url = aws_helper.upload_to_aws(image)
    except:
        return make_response({"error": "Image failed to upload to AWS."}, 500)

    graffiti_obj = graffiti.create_graffiti(image_url=image_url, address=graffiti_data['address'],
                                            longitude=graffiti_data['longitude'], latitude=graffiti_data['latitude'],
                                            zip=graffiti_data['zip'], comment=graffiti_data['comment'])

    return make_response(jsonify(graffiti_obj), 200)


