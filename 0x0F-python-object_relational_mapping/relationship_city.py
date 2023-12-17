#!/usr/bin/python3
"""Defines city class"""
from relationship_state import Base, State
from sqlalchemy import String, Integer, Column, ForeignKey


class City(Base):
    """Base class"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
