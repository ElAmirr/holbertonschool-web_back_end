#!/usr/bin/env python3
""" API app for handling requests with authentication
"""
from flask import Flask, request, abort
from api.v1.auth.auth import Auth
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

auth = None
auth_type = os.getenv('AUTH_TYPE')

# Initialize the Auth object based on AUTH_TYPE
if auth_type == 'auth':
    auth = Auth()

@app.before_request
def before_request():
    """ Filter requests before they are processed """
    if auth is None:
        return

    # Define the list of paths that don't require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    
    # If the request path is in the excluded paths, no need to check authentication
    if request.path in excluded_paths:
        return
    
    # Check if authentication is required for this path
    if auth.require_auth(request.path, excluded_paths):
        # Check for authorization header
        if auth.authorization_header(request) is None:
            abort(401, description="Unauthorized")
        
        # Check for current user
        if auth.current_user(request) is None:
            abort(403, description="Forbidden")

@app.route('/api/v1/status', methods=['GET'])
def status():
    """ API status endpoint """
    return {"status": "OK"}

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """ Unauthorized access endpoint """
    abort(401, description="Unauthorized")

@app.route('/api/v1/forbidden', methods=['GET'])
def forbidden():
    """ Forbidden access endpoint """
    abort(403, description="Forbidden")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
