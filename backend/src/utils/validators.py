import re

GRAFFITI_KEYS = ['address', 'longitude', 'latitude', 'zip', 'comment']
FILE_EXTENSIONS = ['.jpg', '.jpeg', '.png']


def validate_upload_request(request):
    for key in GRAFFITI_KEYS:
        if request[key] == '':
            request[key] = None

    return request


def validate_file_extension(filename):
    extension = re.search(r'\..+', filename)

    if extension.group(0) not in FILE_EXTENSIONS:
        return True

    return False
