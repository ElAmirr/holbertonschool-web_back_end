#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify

# Create a Flask instance
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """
    Home route that returns a JSON response.
    """
    return jsonify({"message": "Bienvenue"})

# Start the app if this module is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
