import base64

class BasicAuth:
    """ Basic Auth class. """

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string.

        Args:
            base64_authorization_header (str): Base64 encoded string.

        Returns:
            str: Decoded UTF-8 string or None if decoding fails.
        """
        if not base64_authorization_header or not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header, validate=True)
            # Convert bytes to UTF-8 string
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
