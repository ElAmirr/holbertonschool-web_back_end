#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

my_db = DB()

# Add a test user
user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

# Find user by email
find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

# Attempt to find a non-existing user
try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

# Attempt to query with an invalid argument
try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")
