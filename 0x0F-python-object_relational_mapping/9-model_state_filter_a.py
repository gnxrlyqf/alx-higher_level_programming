#!/usr/bin/python3
"""Prints all data with the letter a"""
from model_state import State, Base
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
    out = session.query(State).filter(State.name.like("%a%"))
    for state in out:
        print(state.id, state.name, sep=": ")
