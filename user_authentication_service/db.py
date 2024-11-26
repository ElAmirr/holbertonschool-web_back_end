#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The newly created user instance.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to filter the query.

        Returns:
            User: The first user that matches the criteria.

        Raises:
            NoResultFound: If no user matches the criteria.
            InvalidRequestError: If invalid query arguments are provided.
        """
        if not kwargs:
            raise InvalidRequestError("No arguments provided for query.")
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("No user found with the provided criteria.")
        except Exception as e:
            raise InvalidRequestError(f"Invalid query arguments: {kwargs}. Error: {str(e)}")

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes and commit changes to the database.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: The attributes to update and their new values.

        Raises:
            ValueError: If an attribute does not exist in the User model.
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"User has no attribute '{key}'")
            setattr(user, key, value)

        self._session.commit()
