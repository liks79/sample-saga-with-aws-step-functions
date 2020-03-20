"""
    #TITLE
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: 3/16/20
    :description:
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""
import datetime
import pytest
import sqlalchemy
from pytest import yield_fixture
from sqlalchemy.orm import scoped_session, sessionmaker

# from monolithic.model import db
from sqlalchemy import create_engine, Table, MetaData, Column, select, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql.ddl import CreateTable
from sqlalchemy_utc import UtcDateTime, utcnow, utc
from exception import OutOfStockError, PaymentFailureError
import config as conf
from model.order import Order
from model.payment import Payment


def test_db_connection(fx_engine):
    # If there are some issues on DB connection,
    # it will raise sqlalchemy.exc.OperationalError
    connection = fx_engine.connect()
    transaction = connection.begin()
    assert transaction is not None


def test_mock_user(fx_user):
    assert fx_user is not False


def test_mock_inventory(fx_inventory):
    assert fx_inventory is not False


def test_mock_payment(fx_payment_success):
    assert fx_payment_success is not False


def test_mock_order(fx_order):
    assert fx_order is not False


def test_mock_membership(fx_membership):
    assert fx_membership is not False


def test_order_fail_out_of_stock(fx_inventory):
    ordered_qty = 100000000
    current_qty = fx_inventory.qty
    with pytest.raises(OutOfStockError):
        if current_qty - ordered_qty < 0:
            raise OutOfStockError()


def test_order_fail_payment(fx_payment_success):
    fx_payment_success.allowed = False
    with pytest.raises(PaymentFailureError):
        if fx_payment_success.allowed is False:
            raise PaymentFailureError()


def test_order_success(fx_engine, fx_user, fx_inventory,
                       fx_payment_success, fx_order, fx_membership):
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=fx_engine))
    ordered_qty = 1  # sure to succeed

    fx_inventory.qty = fx_inventory.qty - ordered_qty
    session.add(fx_inventory)
    session.add(fx_payment_success)
    session.add(fx_order)
    session.add(fx_membership)
    session.commit()







#
#
#
# def test_order_fail_payment(fx_engine, fx_user, fx_inventory):
#     ordered_item_qty = 1
#     session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=fx_engine))
#     payment = Payment(pay_type='credit_card',
#                       user_id=fx_user.user_id,
#                       allowed=False,
#                       date=utcnow())
#     order = Order(
#         user_id=fx_user.user_id,
#         item_id=fx_inventory.item_id,
#         item_qty=ordered_item_qty,
#         date=utcnow(),
#         deliver_phone=fake.phone_number(),
#         deliver_address=fake.address(),
#         total_price=fake.random_int(100, 1000000))
#
#
#
