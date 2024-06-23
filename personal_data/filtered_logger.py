import logging
import re
import os
import mysql.connector
from typing import List

# Function to filter PII data in a log message
def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    pattern = f"({'|'.join(fields)})=([^ {separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

# Custom logging formatter to redact PII data
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, original_message, self.SEPARATOR)

# PII_FIELDS constant
PII_FIELDS = ("name", "email", "phone", "ssn", "password")

# Function to get a logger configured to redact PII data
def get_logger() -> logging.Logger:
    """Creates a logger with a custom formatter that obfuscates PII fields"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

# Function to get a database connection using credentials from environment variables
def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a MySQL connection object using credentials from environment variables"""
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )

# Main function to retrieve and log user data
def main():
    """Main function that retrieves and logs user data"""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    
    for row in cursor:
        message = "; ".join([f"{key}={value}" for key, value in row.items()])
        logger.info(message)
    
    cursor.close()
    db.close()

# Ensure the main function runs when the module is executed
if __name__ == "__main__":
    main()
