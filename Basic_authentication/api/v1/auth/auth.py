#!/usr/bin/env python3
""" Auth module for API authentication
"""
from flask import request

class Auth:
    """ Auth class to manage authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines whether authentication is required for the given path. """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            if excluded_path.rstrip('/') == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the Authorization header if present, otherwise None """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> None:
        """ Returns None to simulate no current user """
        if request is None:
            return None
        return None
