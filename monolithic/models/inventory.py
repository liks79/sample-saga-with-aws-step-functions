"""
    Database model for transaction of monolithic application
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: 3/12/20
    :description: Database model for monolithic application implementation of simple order transaction scenario
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""
from models import db
from sqlalchemy_utc import UtcDateTime, utcnow
from sqlalchemy import Integer, Float, String, Column


class Inventory(db.Base):
    """
    Database Model class for Inventory table
    """
    __tablename__ = 'Inventory'

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(200), nullable=False)
    price = Column(Float)
    qty = Column(Integer)
    date = Column('date', UtcDateTime, default=utcnow)

    def __init__(self, item_name, price, qty, date):
        self.item_name = item_name
        self.price = price
        self.qty = qty
        self.date = date

    def __repr__(self):
        return '<%r %r %r>' % (self.__tablename__, self.item_id, self.item_name)

    def to_json(self):
        return {
            'item_id': self.item_id,
            'item_name': self.item_name,
            'price': self.price,
            'qty': self.qty,
            'date': self.date
        }
