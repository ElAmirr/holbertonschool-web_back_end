#!/usr/bin/env python3
"""
Filtering log data module.

This module provides a utility function for obfuscating sensitive fields
in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): String to replace the field values with.
        message (str): The log message to process.
        separator (str): Separator character in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = r'(' + '|'.join(re.escape(field) for field in fields) + r')=[^' + re.escape(separator) + r']*'
    return re.sub(pattern, lambda match: match.group(1) + '=' + redaction, message)
