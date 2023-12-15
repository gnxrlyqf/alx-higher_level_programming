#!/usr/bin/python3
"""Prints data that starts with N in a database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor._query("SELECT * FROM states WHERE name LIKE 'N%'")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
