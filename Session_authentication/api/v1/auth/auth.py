#!/usr/bin/env python3
""" Auth module for API authentication
"""
from typing import List
from flask import request


class Auth:
    """ Auth class to manage authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if path is not in excluded_paths, considering the path may or may not have a trailing slash.
        Returns True if path is None or excluded_paths is None or empty.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        
        # Remove trailing slash for comparison
        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            if excluded_path.rstrip('/') == path:
                return False
        
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header if it exists, otherwise None.
        """
        if request is None:
            return None
        # Check if the Authorization header exists
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> None:
        """
        Returns None, which simulates no current user being set.
        """
        if request is None:
            return None
        return None
