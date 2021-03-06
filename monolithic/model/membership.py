"""
    Database model for transaction of monolithic application
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Friday, March 13, 2020
    :description: Database model for monolithic application implementation of simple order transaction scenario
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""
from model import db
from model.user import User
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy_utc import UtcDateTime, utcnow


class Membership(db.Base):
    """
    Database Model class for Membership table
    """
    __tablename__ = 'Membership'

    seq_id = Column(Integer, primary_key=True)
    user_id = Column(String(100), ForeignKey(User.user_id, ondelete='cascade'))
    date = Column('date', UtcDateTime, default=utcnow)
    mileage = Column(Integer)

    def __init__(self, user_id, date, mileage):
        self.user_id = user_id
        self.date = date
        self.mileage = mileage

    def __repr__(self):
        return '<%r %r %r>' % (self.__tablename__, self.seq_id, self.user_id)

    def to_json(self):
        return {
            'seq_id': self.seq_id,
            'user_id': self.user_id,
            'date': self.date,
            'mileage': self.mileage
        }
