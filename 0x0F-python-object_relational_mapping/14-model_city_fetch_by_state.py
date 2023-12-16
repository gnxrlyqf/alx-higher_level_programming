#!/usr/bin/python3
"""Prints all data in database"""
from model_state import State, Base
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()
    out = (session.query(
        State.name,
        City.id,
        City.name
    ).filter(State.id == City.state_id))
    for city in out:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
    session.close()
