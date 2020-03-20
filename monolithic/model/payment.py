"""
    #TITLE
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: 3/12/20
    :description:
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""
from model import db
from model.user import User
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy_utc import UtcDateTime, utcnow


class Payment(db.Base):
    """
    Database Model class for Payment table
    """
    __tablename__ = 'Payment'

    pay_id = Column(Integer, primary_key=True)
    user_id = Column(String(100), ForeignKey(User.user_id, ondelete='cascade'))
    pay_type = Column(String(200))
    allowed = Column(Boolean)
    date = Column('date', UtcDateTime, default=utcnow)

    def __init__(self, user_id, pay_type, allowed, date):
        self.user_id = user_id
        self.pay_type = pay_type
        self.allowed = allowed
        self.date = date

    def __repr__(self):
        return '<%r %r %r>' % (self.__tablename__, self.pay_id, self.user_id)

    def to_json(self):
        return {
            'pay_id': self.pay_id,
            'user_id': self.user_id,
            'type': self.pay_type,
            'allowed': self.allowed,
            'date': self.date
        }
