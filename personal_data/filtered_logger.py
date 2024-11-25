#!/usr/bin/env python3
"""
Module for obfuscating log messages.

This module provides the `filter_datum` function for obfuscating sensitive
information in log messages using regex.
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
        separator (str): The character separating the fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = '|'.join([f"{field}=[^\\{separator}]*" for field in fields])
    return re.sub(pattern, lambda match: f"{match.group().split('=')[0]}={redaction}", message)
