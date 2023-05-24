#!/usr/bin/env python3
"""
Filtered Logger module
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specified fields in a log message
    """
    return re.sub(r'(?<=\b' + separator + '|^)(' + '|'.join(fields) + ')=.*?(?=' + separator + '|$)', lambda match: match.group(1) + '=' + redaction, message)


if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
                "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))

