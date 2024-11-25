#!/usr/bin/env python3
""" Basic Auth module for API authentication
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth
    """
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decode Base64 string."""
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract user email and password from decoded Base64 string."""
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Retrieve User instance based on email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            user = users[0]
            if not user.is_valid_password(user_pwd):
                return None
            return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overload Auth's `current_user` method to retrieve User instance for the request.

        Steps:
        1. Retrieve Authorization header.
        2. Extract Base64 part from Authorization header.
        3. Decode Base64 string.
        4. Extract user credentials (email, password).
        5. Retrieve User instance based on credentials.
        """
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_authorization_header = self.extract_base64_authorization_header(authorization_header)
        if base64_authorization_header is None:
            return None

        decoded_base64 = self.decode_base64_authorization_header(base64_authorization_header)
        if decoded_base64 is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_base64)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
