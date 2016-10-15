# -*- coding: utf-8 -*-
"""DB models."""
import datetime as dt

from hackvt2016.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Resource(SurrogatePK, Model):
    """A resource."""

    __tablename__ = 'resources'
    title = Column(db.String, nullable=False)
    description = Column(db.String, nullable=False)
    host = Column(db.String, nullable=True)
    email = Column(db.String, nullable=True)
    longitude = Column(db.Float, nullable=True)
    latitude = Column(db.Float, nullable=True)

    category_id = reference_col('categories', nullable=False)


