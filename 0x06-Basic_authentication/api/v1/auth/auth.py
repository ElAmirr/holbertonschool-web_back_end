#!/usr/bin/env python3
""" Auth
"""

import re
from flask import request


class Auth:
    """ Auth class doc
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return None

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None