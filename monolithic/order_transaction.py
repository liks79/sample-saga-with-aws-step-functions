"""
    Database model for Monolithic application
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Thursday, March 12, 2020
    :description: Monolithic application implementation of simple order transaction scenario
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""
import config
import traceback
from model import db
from model.user import User
from model.order import Order
from model.membership import Membership
from model.payment import Payment
from model.inventory import Inventory
from faker import Faker
from pprint import pformat
from sqlalchemy_utc import utcnow
from exception import OutOfStockError, PaymentFailureError

fake = Faker(config.FAKER_LOCALE)
logger = config.logger

try:
    """ Data Preparation """
    # Create tables, if it is not existed.
    db.Base.metadata.create_all(bind=db.engine)

    # T0.TRANSACTION BEGIN
    # Transaction is already begun by SQLalchemy
    logger.info('#### T0.TRANSACTION BEGIN ####')

    # T1.Initiate User model
    logger.info('#### T1.INITIATE USER MODEL ####')
    user = db.session.query(User).first()
    logger.info(pformat(user.to_json()))

    # T2.Initiate Inventory model
    logger.info('#### T2.INITIATE INVENTORY MODEL ####')
    item = db.session.query(Inventory).first()
    logger.info(pformat(item.to_json()))

    # T3.Initiate Payment model
    logger.info('#### T3.INITIATE PAYMENT MODEL ####')
    payment = Payment(pay_type='credit_card',
                      user_id=user.user_id,
                      allowed=fake.boolean(),
                      date=utcnow())
    logger.info(pformat(payment.to_json()))
    db.session.add(payment)
    # db.session.commit()

    # T4.Initiate Order model
    logger.info('#### T4.INITIATE ORDER MODEL ####')
    ordered_item_qty = fake.random_int(1, 100)
    order = Order(user_id=user.user_id,
                  item_id=item.item_id,
                  item_qty=ordered_item_qty,
                  date=utcnow(),
                  deliver_phone=fake.phone_number(),
                  deliver_address=fake.address(),
                  total_price=fake.random_int(100, 1000000))
    logger.info(pformat(order.to_json()))
    db.session.add(order)
    # db.session.commit()

    # T5.Update Inventory model
    logger.info('#### T5.UPDATE INVENTORY MODEL ####')
    logger.info('UPDATE INVENTORY QTY: {} - {} = {}'.
                format(item.qty, ordered_item_qty, item.qty - ordered_item_qty))
    item.qty = item.qty - ordered_item_qty

    # T6.Update Membership model
    membership = Membership(user_id=user.user_id,
                            date=utcnow(),
                            mileage=fake.random_int(10, 400))
    db.session.add(membership)
    logger.info('#### T6.UPDATE MEMBERSHIP ####')
    logger.info(pformat(membership.to_json()))

    # OutOfStockError Exception handling
    logger.info(pformat(item.to_json()))
    if item.qty < 0:
        logger.error('ORDERED ITEM IS OUT OF STOCK: %s' % item.qty)
        logger.error('THIS IS AN INTENDED ERROR.')
        raise OutOfStockError

    # PaymentFailureError Exception handling
    logger.info(pformat(payment.to_json()))
    if payment.allowed is not True:
        logger.error('PAYMENT TRANSACTION IS FAILED: %s' % payment.allowed)
        logger.error('THIS IS AN INTENDED ERROR.')
        raise PaymentFailureError

    # T7.Commit
    db.session.commit()
    logger.info('#### T7.TRANSACTION COMPLETED! ####')

except Exception as e:
    logger.error(e)
    print(traceback.format_exc())
    db.session.rollback()

finally:
    db.session.close()
