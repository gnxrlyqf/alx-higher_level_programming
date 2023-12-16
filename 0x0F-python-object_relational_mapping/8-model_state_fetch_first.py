#!/usr/bin/python3
"""Prints first row in database"""
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
    out = session.query(State).first()
    if out is not None:
        print(out.id, out.name, sep=": ")
    else:
        print("Nothing")
    session.close()
