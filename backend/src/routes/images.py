from flask import Blueprint, jsonify
from flask import make_response, request
from backend.src.utils import aws_helper
from backend.src.crud import graffiti
from backend.src.utils.decorators import admin_rights_required, is_admin


images = Blueprint("images", __name__)


@images.route("/api/v1/images", methods=["POST"])
def upload_image():
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


@images.route("/api/v1/images", methods=["GET"])
@is_admin
def retrieve_images(has_admin_valid_token):
    return make_response(jsonify(graffiti.get_graffities(has_admin_valid_token)), 200)


@images.route("/api/v1/images/<id>", methods=["GET", "PATCH"])
@admin_rights_required
def retrieve_image(id):
    if request.method == "GET":
        graffiti_obj = graffiti.get_graffiti(id)
        if graffiti_obj:
            return make_response(jsonify(graffiti_obj), 200)
        else:
            err = "User with the " + str(id) + " is not found."
            return make_response(jsonify({"error": err}), 404)

    elif request.method == "PATCH":
        params = request.get_json()

        if "has_admin_checked" in params.keys():
            changed_graffiti_id = graffiti.check_graffiti(id)
            return make_response(jsonify({"id": changed_graffiti_id, "message": "The graffiti object has been patched."}), 200)
        else:
            return make_response(jsonify({"error": "Cannot patch the resource with this data."}), 400)

