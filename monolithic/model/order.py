"""
    Database model for transaction of monolithic application
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Thursday, March 12, 2020
    :description: Database model for monolithic application implementation of simple order transaction scenario
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""

from model import db
from model.user import User
from model.inventory import Inventory
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy_utc import UtcDateTime, utcnow


class Order(db.Base):
    """
    Database Model class for Order table
    """
    __tablename__ = 'Order'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(String(100), ForeignKey(User.user_id, ondelete='cascade'))
    item_id = Column(Integer, ForeignKey(Inventory.item_id, ondelete='cascade'))
    item_qty = Column(Integer, default=1)
    date = Column('date', UtcDateTime, default=utcnow)
    deliver_phone = Column(String(50), unique=True)
    deliver_address = Column(String(200))
    total_price = Column(Integer)

    def __init__(self, user_id, item_id, item_qty, date, deliver_phone, deliver_address, total_price):
        self.user_id = user_id
        self.item_id = item_id
        self.item_qty = item_qty
        self.date = date
        self.deliver_phone = deliver_phone
        self.deliver_address = deliver_address
        self.total_price = total_price

    def __repr__(self):
        return '<%r %r %r>' % (self.__tablename__, self.order_id, self.user_id)

    def to_json(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'item_id': self.item_id,
            'item_qty': self.item_qty,
            'date': self.date,
            'deliver_phone': self.deliver_phone,
            'deliver_address': self.deliver_address,
            'total_price': self.total_price
        }
