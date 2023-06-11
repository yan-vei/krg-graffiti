from flask import Blueprint, jsonify
from flask import make_response, request
from backend.src.utils import aws_helper
from backend.src.crud import graffiti
from backend.src.utils.decorators import admin_rights_required, is_admin
from backend.src.utils.validators import validate_upload_request


images = Blueprint("images", __name__)


@images.route("/api/v1/images", methods=["POST"])
def upload_image():
    graffiti_data = request.form.to_dict()

    graffiti_data = validate_upload_request(graffiti_data)

    image = request.files['image']

    try:
        image_url = aws_helper.upload_to_aws(image)
    except Exception as e:
        return make_response({"error": "Image failed to upload to AWS."}, 500)

    graffiti_obj = graffiti.create_graffiti(image_url=image_url, address=graffiti_data['address'],
                                            longitude=graffiti_data['longitude'], latitude=graffiti_data['latitude'],
                                            zip=graffiti_data['zip'], comment=graffiti_data['comment'])

    return make_response(jsonify(graffiti_obj), 200)


@images.route("/api/v1/images", methods=["GET"])
@is_admin
def retrieve_images(has_admin_valid_token):
    return make_response(jsonify(graffiti.get_graffities(has_admin_valid_token)), 200)


@images.route("/api/v1/images/<id>", methods=["GET", "PATCH"])
@admin_rights_required
def retrieve_image(id):
    graffiti_obj = graffiti.get_graffiti(id)

    if graffiti_obj == {}:
        err = "Graffiti with the id " + str(id) + " is not found."
        return make_response(jsonify({"error": err}), 404)

    if request.method == "GET":
        return make_response(jsonify(graffiti_obj), 200)

    elif request.method == "PATCH":
        params = request.get_json()

        changed_graffiti_id = graffiti.update_graffiti(id, params)
        return make_response(jsonify({"id": changed_graffiti_id, "message": "The graffiti object has been patched."}),
                             200)
