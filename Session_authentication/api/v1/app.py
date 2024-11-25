#!/usr/bin/env python3
""" Main module for the Flask API
"""
from flask import Flask, request, abort
from flask_cors import CORS
import os

# Import the Auth classes
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
CORS(app)

# Initialize auth variable
auth = None

# Load the correct authentication class based on the AUTH_TYPE environment variable
auth_type = os.getenv('AUTH_TYPE')

if auth_type == 'basic_auth':
    auth = BasicAuth()
else:
    auth = Auth()

# Method to handle before_request for request validation
@app.before_request
def before_request():
    """
    This method runs before each request.
    It validates the request for authorization and current user.
    """
    if auth is None:
        return

    # List of paths that do not require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if request.path not in excluded_paths:
        # Check if authentication is required
        if auth.require_auth(request.path, excluded_paths):
            # Check if the authorization header is present
            if auth.authorization_header(request) is None:
                abort(401)  # Unauthorized

            # Check if the current user is valid
            if auth.current_user(request) is None:
                abort(403)  # Forbidden

# Routes definition
@app.route('/api/v1/status', methods=['GET'])
def status():
    """Returns the status of the API"""
    return {'status': 'OK'}

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Returns an unauthorized error"""
    abort(401)

@app.route('/api/v1/forbidden', methods=['GET'])
def forbidden():
    """Returns a forbidden error"""
    abort(403)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    """Returns a list of users (example route)"""
    return {"users": []}, 200


if __name__ == '__main__':
    api_host = os.getenv('API_HOST', '0.0.0.0')
    api_port = os.getenv('API_PORT', 5000)
    app.run(host=api_host, port=api_port)
