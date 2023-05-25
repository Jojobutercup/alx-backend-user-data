#!/usr/bin/env python3
"""
Filtered Logger module
"""

from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    """
    Replace field values in a log message with a redaction string
    """
    regex = r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator)
    return re.sub(
            regex,
            lambda match: match.group().split('=')[0] + '=' + redaction,
            message
    )
