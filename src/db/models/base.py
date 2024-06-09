"""
Base module for all database models.

The Base is a base class which stores a catalog of classes
and mapped tables in the Declarative system.
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
