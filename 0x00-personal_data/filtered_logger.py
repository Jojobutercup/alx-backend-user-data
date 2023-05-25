#!/usr/bin/env python3
"""
Filtered Logger module
"""

import logging
import csv
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by redacting specified fields
        """
        message = super().format(record)
        for field in PII_FIELDS:
            message = message.replace(field, self.REDACTION)
        return message


def get_logger() -> logging.Logger:
    """
    Create and configure a logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = RedactingFormatter(
            "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def read_file(filename: str) -> List[dict]:
    """
    Read a CSV file and return its content as a list of dictionaries
    """
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(dict(row))
    return data
