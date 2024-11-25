import base64

class BasicAuth:
    """ Basic Authentication class """

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string.
        
        Args:
            base64_authorization_header (str): The Base64 encoded string.
        
        Returns:
            str: Decoded string as UTF-8 or None if invalid input.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
