#!/usr/bin/env python3
"""
Encrypt Password module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the given password using bcrypt.

    Args:
        password: The password to be hashed.

    Returns:
        The salted, hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    print(hash_password(password))
    print(hash_password(password))
