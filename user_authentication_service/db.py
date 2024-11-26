def add_user(self, email: str, hashed_password: str) -> User:
    """Adds a user to the database"""
    new_user = User(email=email, hashed_password=hashed_password)
    self._session.add(new_user)
    self._session.commit()
    return new_user
