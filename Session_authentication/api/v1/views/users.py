from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a user by ID or the authenticated user if 'me'"""
    if user_id == "me":
        # If the user ID is 'me', return the authenticated user's info
        if request.current_user is None:
            abort(404)  # Not found
        return jsonify(request.current_user.to_dict())

    # Normal behavior for other user IDs
    user = User.get(user_id)
    if user is None:
        abort(404)  # Not found
    return jsonify(user.to_dict())
