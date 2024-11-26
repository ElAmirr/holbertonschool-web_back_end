#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user if the email does not already exist.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            User: The created user object.

        Raises:
            ValueError: If a user with the provided email already exists.
        """
        try:
            # Check if user already exists
            self._db.find_user_by(email=email)
            # If found, raise an error
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If not found, proceed with creating the user
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password.decode('utf-8'))
