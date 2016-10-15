# -*- coding: utf-8 -*-
"""DB models."""
import datetime as dt

from hackvt2016.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Location(SurrogatePK, Model):
    """A location."""

    __tablename__ = 'locations'
    address = Column(db.String, nullable=True)
    longitude = Column(db.String, nullable=False)
    latitude = Column(db.String, nullable=False)
