from typing import TypeVar
from models.user import User


class BasicAuth:
    """ Basic Auth class. """

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance if credentials are valid, otherwise None.
        """
        if not user_email or not isinstance(user_email, str):
            return None

        if not user_pwd or not isinstance(user_pwd, str):
            return None

        # Look up user by email
        user = User.search({'email': user_email})
        if not user or len(user) == 0:
            return None

        user_instance = user[0]  # Assuming `search` returns a list

        # Verify password
        if not user_instance.is_valid_password(user_pwd):
            return None

        return user_instance
