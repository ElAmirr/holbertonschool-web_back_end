#!/usr/bin/env python3
"""
Module for handling sensitive information in logs.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Replaces sensitive information in a log message with a redaction string.

    Args:
        fields (List[str]): The fields to obfuscate.
        redaction (str): The string to replace the sensitive data with.
        message (str): The log message to be filtered.
        separator (str): The field separator in the log message.

    Returns:
        str: The log message with sensitive fields redacted.
    """
    pattern = f"({'|'.join(re.escape(field) for field in fields)})=.*?{re.escape(separator)}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)
