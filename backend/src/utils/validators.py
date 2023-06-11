GRAFFITI_KEYS = ['address', 'longitude', 'latitude', 'zip', 'comment']


def validate_upload_request(request):
    for key in GRAFFITI_KEYS:
        if request[key] == '':
            request[key] = None

    return request