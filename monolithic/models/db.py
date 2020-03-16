"""
    Database init configuration
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: 3/13/20
    :description: Database init config
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import config as conf

Base = declarative_base()
engine = create_engine(conf.DB_URI, echo=conf.SQLALCHEMY_ECHO, connect_args={"options": "-c timezone=utc"})

# create a Session
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))




