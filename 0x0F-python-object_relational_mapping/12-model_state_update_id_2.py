#!/usr/bin/python3
"""Changes the name of a state"""
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
    out = session.query(State).filter(State.id == 2).first()
    out.name = "New Mexico"
    session.commit()
    session.close()
