#!/usr/bin/env python3
"""
Module for filtering log messages.

This module provides a function to obfuscate sensitive information
in log messages based on given fields.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): A list of strings representing fields to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log message to be obfuscated.
        separator (str): The character separating fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=[^\\{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
