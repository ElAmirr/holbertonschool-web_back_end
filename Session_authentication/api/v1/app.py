from flask import Flask, jsonify, request, abort
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
auth = None

if AUTH_TYPE == "basic_auth":
    auth = BasicAuth()

@app.before_request
def before_request():
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    request.current_user = auth.current_user(request)
    if request.current_user is None:
        abort(403)
