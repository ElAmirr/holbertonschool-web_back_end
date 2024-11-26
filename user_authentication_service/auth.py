import uuid

class Auth:
    """Auth class to interact with the authentication database."""
    
    def __init__(self):
        # Initialize any necessary variables or database connections
        pass
    
    def _generate_uuid(self) -> str:
        """Generates and returns a new UUID as a string."""
        return str(uuid.uuid4())
