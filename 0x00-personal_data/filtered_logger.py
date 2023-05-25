#!/usr/bin/env python3
"""
Filtered Logger module
"""

import os
import mysql.connector
from mysql.connector import errorcode


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database and return a connection object
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    try:
        db = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        return db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Refer to database credentials.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: The specified database does not exist.")
        else:
            print("Error: Failed to connect to the database.")
        exit(1)
