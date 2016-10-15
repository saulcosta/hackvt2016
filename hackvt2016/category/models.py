# -*- coding: utf-8 -*-
"""DB models."""
import datetime as dt

from hackvt2016.database import Column, Model, SurrogatePK, db, reference_col, relationship

class Category(SurrogatePK, Model):
    """A category."""

    __tablename__ = 'categories'
    name = Column(db.String(80), unique=True, nullable=False)
    icon = Column(db.String(80), unique=True, nullable=False)
    color = Column(db.String(80), unique=True, nullable=False)
