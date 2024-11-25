#!/usr/bin/env python3
"""
Module for filtering sensitive data in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): Redaction string.
        message (str): Log message to be filtered.
        separator (str): Separator in the log message.

    Returns:
        str: Obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)
