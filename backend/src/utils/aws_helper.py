import imghdr
import uuid
from io import BytesIO
import boto3
from backend.src import config


AWS_ACCESS_KEY = config.AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
AWS_BUCKET_NAME = config.AWS_BUCKET_NAME


def get_file_extension(file_name, decoded_file):
    extension = imghdr.what(file_name, decoded_file)
    extension = "jpg" if extension == "jpeg" else extension
    return extension


def upload_to_aws(image_file):
    file = BytesIO(image_file.read())
    file_name = str(uuid.uuid4())[:12]

    client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    client.upload_fileobj(
        file,
        AWS_BUCKET_NAME,
        file_name,
        ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/png'}
    )
    location = client.get_bucket_location(Bucket=AWS_BUCKET_NAME)['LocationConstraint']
    object_url = "https://%s.s3-%s.amazonaws.com/%s" % (AWS_BUCKET_NAME, location, file_name)
    return object_url
