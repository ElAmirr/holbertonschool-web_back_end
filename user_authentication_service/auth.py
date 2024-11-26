#!/usr/bin/env python3
"""
Auth class to handle user authentication
"""
from db import DB
from bcrypt import hashpw, checkpw, gensalt
from user import User

class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize Auth object."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user by storing the email and hashed password."""
        hashed_password = _hash_password(password)
        try:
            user = self._db.add_user(email, hashed_password)
            return user
        except ValueError:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user credentials by checking the password."""
        try:
            # Locate the user by email
            user = self._db.find_user_by(email=email)

            # Check if the password matches the stored hashed password
            if checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
                return True
            return False
        except NoResultFound:
            return False
        except InvalidRequestError:
            return False

def _hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
