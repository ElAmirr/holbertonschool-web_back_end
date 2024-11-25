#!/usr/bin/env python3
""" Filtered Logger Module """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: A list of strings representing fields to obfuscate.
        redaction: The string to replace field values with.
        message: The log line to be obfuscated.
        separator: The character separating fields in the log line.

    Returns:
        A string with specified fields obfuscated.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
