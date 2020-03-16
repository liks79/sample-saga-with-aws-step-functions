"""
    Database models for Monolithic application
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Thursday, March 12, 2020
    :description: Monolithic application implementation of simple order transaction scenario
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""
import sys
import config
from faker import Faker
from pprint import pformat
from models import db
from models.user import User
from models.order import Order
from models.membership import Membership
from models.payment import Payment
from models.inventory import Inventory
from sqlalchemy_utc import utcnow

faker = Faker(config.FAKER_LOCALE)
logger = config.logger

try:
    """ Data Preparation """
    # Create tables, if it is not existed.
    db.Base.metadata.create_all(bind=db.engine)

    # T1.Initiate User model
    user = db.session.query(User).first()
    logger.debug('CHOOSE A SOMEONE IN THE USER TABLE WHO WANT TO ORDER AN ITEM.')
    logger.info(pformat(user.to_json()))

    # T2.Initiate Inventory model
    item = db.session.query(Inventory).first()
    logger.debug('CHOOSE AN ITEM WHICH SOMEONE WANT TO BUY.')
    logger.info(pformat(item.to_json()))

    # T3.Initiate Payment model
    payment = Payment(pay_type='credit_card',
                      allowed=True,
                      date=utcnow())
    logger.debug('CREATE PAYMENT..')
    logger.info(pformat(payment.to_json()))
    db.session.add(payment)

    # T4.Initiate Order model
    ordered_item_qty = faker.random_int(1, 100)
    order = Order(
        user_id=user.user_id,
        item_id=item.item_id,
        item_qty=ordered_item_qty,
        pay_id=payment.pay_id,
        date=utcnow(),
        deliver_phone=faker.phone_number(),
        deliver_address=faker.address(),
        total_price=faker.random_int(100, 1000000))

    logger.debug('CREATE ORDER..')
    logger.info(pformat(order.to_json()))
    db.session.add(order)

    # T5.Update Inventory model
    logger.debug('UPDATE INVENTORY QTY: {} - {} = ()'.
                 format(item.qty, ordered_item_qty, item.qty+ordered_item_qty))
    item.qty = item.qty - ordered_item_qty
    logger.info(pformat(item.to_json()))

    # T6.Update Membership model
    membership = Membership(
        user_id=user.user_id,
        order_id=order.order_id,
        date=utcnow(),
        mileage=faker.random_int(10, 400)
    )
    db.session.add(membership)
    logger.debug('UPDATE MEMBERSHIP..')
    logger.info(pformat(membership.to_json()))

    # T7.Commit all
    db.session.commit()
    logger.info('TRANSACTION COMPLETED!')

except Exception as e:
    logger.error(e)
    db.session.rollback()

finally:
    db.session.close()
