# -*- coding: utf-8 -*-
"""DB models."""
import datetime as dt

from hackvt2016.database import Column, Model, SurrogatePK, db, reference_col, relationship

class Category(SurrogatePK, Model):
    """A category."""

    __tablename__ = 'categories'
    name = Column(db.String(80), unique=True, nullable=False)
    icon = Column(db.String(80), unique=True, nullable=False)


class Location(SurrogatePK, Model):
    """A location."""

    __tablename__ = 'locations'
    address = Column(db.String, nullable=True)
    longitude = Column(db.String, nullable=False)
    latitude = Column(db.String, nullable=False)


class Resource(SurrogatePK, Model):
    """A resource."""

    __tablename__ = 'resources'
    title = Column(db.String, nullable=False)
    description = Column(db.String, nullable=False)
    host = Column(db.String, nullable=True)
    email = Column(db.String, nullable=True)

    category_id = reference_col('categories', nullable=False)
    location_id = reference_col('locations', nullable=False)


