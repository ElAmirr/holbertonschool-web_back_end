#!/usr/bin/env python3
"""
Module for handling sensitive data in logs and database connections.
"""

import re
import logging
import os
from typing import List, Tuple
import mysql.connector


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
    pattern = f"({'|'.join(re.escape(field) for field in fields)})=.*?{re.escape(separator)}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for filtering sensitive information.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message, self.SEPARATOR)


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Creates a logger for personal data.

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to a secure database using environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object.
    """
    try:
        return mysql.connector.connect(
            host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
            user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
            password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
            database=os.getenv("PERSONAL_DATA_DB_NAME", "test_db")
        )
    except mysql.connector.Error as err:
        raise ConnectionError(f"Database connection failed: {err}")
