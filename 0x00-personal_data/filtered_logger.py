#!/usr/bin/env python3
"""
Filtered Logger module
"""

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by redacting specified fields
        """
        message = record.getMessage()
        for field in self.fields:
            regex = r'({})=([^{}]+)'.format(field, self.SEPARATOR)
            message = re.sub(regex, r'\1=' + self.REDACTION, message)
        record.message = message
        return super().format(record)
