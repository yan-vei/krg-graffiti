from functools import wraps
from flask import make_response, request, jsonify
from src.config import ADMIN_TOKEN


def is_admin(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        has_valid_admin_token = False
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return f(has_valid_admin_token, *args, **kwargs)
        elif token != ADMIN_TOKEN:
            return f(has_valid_admin_token, *args, **kwargs)
        has_valid_admin_token = True
        return f(has_valid_admin_token, *args, **kwargs)
    return decorator


def admin_rights_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({"error": "A valid token is missing."}), 401)
        elif token != ADMIN_TOKEN:
            return make_response(jsonify({"error": "Token is invalid."}), 403)
        return f(*args, **kwargs)
    return decorator
