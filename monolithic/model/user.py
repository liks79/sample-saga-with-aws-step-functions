"""
    Database model for transaction of monolithic application
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Friday, March 13, 2020
    :description: Database model for monolithic application implementation of simple order transaction scenario
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""

from model import db
from sqlalchemy import String, Column
from sqlalchemy_utc import UtcDateTime, utcnow


class User(db.Base):
    """
    Database Model class for User table
    """
    __tablename__ = 'User'

    user_id = Column(String(100), primary_key=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(50), unique=True)
    address = Column(String(200), nullable=False)
    date = Column('date', UtcDateTime, default=utcnow)

    def __init__(self, user_id, password, email, first_name, last_name, phone, address, date):
        self.user_id = user_id
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.date = date

    def __repr__(self):
        return '<%r %r %r>' % (self.__tablename__, self.user_id, self.email)

    def to_json(self):
        return {
            'user_id': self.user_id,
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'address': self.address,
            'date': self.date
        }
