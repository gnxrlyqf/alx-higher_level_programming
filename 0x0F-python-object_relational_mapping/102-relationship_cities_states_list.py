#!/usr/bin/python3
"""Prints all data in database"""
from relationship_state import State, Base
from relationship_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
    ))
    Session = sessionmaker(bind=engine)
    session = Session()

    for obj in session.query(State):
        for city in obj.cities:
            print(city.id, city.name, sep=": ", end="")
            print(" -> " + obj.name)
    session.close()
