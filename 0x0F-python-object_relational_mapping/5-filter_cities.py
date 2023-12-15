#!/usr/bin/python3
"""Prints data in a database"""
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
    cursor._query("""
        SELECT DISTINCT cities.name FROM cities WHERE state_id IN (
            SELECT id FROM states WHERE name = '{}'
        )
    """.format(sys.argv[4]))
    data = cursor.fetchall()
    out = list(row[0] for row in data)
    print(*out, sep=", ")
    cursor.close()
    db.close()
