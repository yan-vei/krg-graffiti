import imghdr
import io
import uuid
import boto3
from backend.src import config
import base64


AWS_ACCESS_KEY = config.AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
AWS_BUCKET_NAME = config.AWS_BUCKET_NAME


def get_file_extension(file_name, decoded_file):
    extension = imghdr.what(file_name, decoded_file)
    extension = "jpg" if extension == "jpeg" else extension
    return extension


def decode_base64_file(data):
    try:
        decoded_file = base64.b64decode(data)
    except TypeError:
        TypeError('invalid_image')

    file_name = str(uuid.uuid4())[:12]
    file_extension = get_file_extension(file_name, decoded_file)

    complete_file_name = "%s.%s" % (file_name, file_extension,)

    return io.BytesIO(decoded_file), complete_file_name


def upload_to_aws(base64_image):
    file, file_name = decode_base64_file(base64_image)
    client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    client.upload_fileobj(
        file,
        AWS_BUCKET_NAME,
        file_name,
        ExtraArgs={'ACL': 'public-read'}
    )
    location = client.get_bucket_location(Bucket=AWS_BUCKET_NAME)['LocationConstraint']
    object_url = "https://%s.s3-%s.amazonaws.com/%s" % (AWS_BUCKET_NAME, location, file_name)
    return object_url
