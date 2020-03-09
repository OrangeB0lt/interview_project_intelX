#!/usr/bin/python3
"""
Project sqlalchemy object
"""

from datetime import datetime
import uuid
import sys
from sqlalchemy import Column, String, Table, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import storage

time = "%Y-%m-%d|%H:%M:%S"
Base = declarative_base()

class Project(Base):
    """
    The Project class which is a skeleton of project
    """

    """
    sqlalchemy variable mappingsin __get__
    obj.__dict__[self.__name__] = result = self.fget(obj)

    """
    projects = Table(
        'projects', MetaData(),
        project_id = Column(String(128), nullable=False, primary_key=True),
        name = Column(String(128), nullable=False),
        creation_date = Column(String(128), nullable=False)
    )

    users = Table(
        'users', MetaData(),
        user_id = Column(String(128), nullable=False, primary_key=True),
        u_name = Column(String(128), nullable=False),
        u_email = Column(String(128), nullable=False)
    )

    files = Table(
        'files', MetaData(),
        f_id = Column(String(128), nullable=False, primary_key=True),
        f_name = Column(String(128), nullable=False),
        f_type = Column(String(128), nullable=False)

    )

    def __init__(self, name, project_id, creation_date, user_name, file_name, user_id, u_name, u_email, f_id, f_name, f_type):
        """
        Class constructor
        """
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.user_name = user_name
        self.file_name = file_name
        self.creation_date = datetime.strftime(datetime.utcnow(), time)
        self.user_id = user_id
        self.u_name = u_name
        self.u_email = u_email
        self.f_id = f_id
        self.f_name = f_name
        self.f_type = f_type

    def save(self):
        """
        Uses storage engine to save self instance
        """
        storage.storage_instance.new(self)
        storage.storage_instance.save()

    def to_dict(self):
        """
        return dictionary representation
        """
        dict_copy = self.__dict__.copy()
        return dict_copy