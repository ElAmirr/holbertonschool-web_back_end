#!/usr/bin/env python3
""" Auth module for API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class to manage authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False if the path is in excluded_paths, True otherwise.
        """
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns None, which simulates no authorization header.
        """
        if request is None:
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None, which simulates no current user being set.
        """
        if request is None:
            return None
        return None
