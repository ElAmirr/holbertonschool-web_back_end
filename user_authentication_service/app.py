from flask import Flask, request, jsonify, abort, make_response
from auth import Auth
import uuid

app = Flask(__name__)

AUTH = Auth()

@app.route("/sessions", methods=["POST"])
def login():
    """Handles the login functionality."""
    email = request.form.get("email")
    password = request.form.get("password")

    # Check if the email and password are provided
    if not email or not password:
        abort(400, description="Missing email or password")

    # Check if credentials are valid
    if not AUTH.valid_login(email, password):
        abort(401, description="Unauthorized")

    # Create a session ID (simulate a session creation here)
    session_id = str(uuid.uuid4())

    # Store the session ID as a cookie in the response
    response = make_response(
        jsonify({"email": email, "message": "logged in"})
    )
    response.set_cookie("session_id", session_id)

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
