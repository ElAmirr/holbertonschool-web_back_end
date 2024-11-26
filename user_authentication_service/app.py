#!/usr/bin/env python3
"""
Basic Flask app with user registration
"""
from flask import Flask, jsonify, request
from auth import Auth

# Initialize the Auth class
AUTH = Auth()

# Create a Flask instance
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """
    Home route that returns a JSON response.
    """
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def register_user():
    """
    Endpoint to register a new user.
    """
    # Ensure email and password are provided in the form data
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        # If either email or password is missing, return an error response
        return jsonify({"message": "email and password required"}), 400

    try:
        # Attempt to register the user using the Auth class
        user = AUTH.register_user(email, password)

        # Return a successful JSON response with user email
        return jsonify({"email": user.email, "message": "user created"}), 201

    except ValueError as err:
        # Handle user already exists case
        return jsonify({"message": str(err)}), 400

# Start the app if this module is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
