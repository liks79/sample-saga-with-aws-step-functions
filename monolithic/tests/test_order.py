"""
    #TITLE
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: 3/16/20
    :description:
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""

from pytest import yield_fixture
from sqlalchemy.orm import scoped_session, sessionmaker

# from monolithic.model import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from monolithic import config as conf


# @fixture(scope='function')
# def fx_tables():
#     engine = create_engine(url, poolclass=NullPool)
#     request.addfinalizer(engine.dispose)
#     return engine

@yield_fixture
def fx_tables(fx_engine):
    from monolithic.model.inventory import Inventory
    from monolithic.model.membership import Membership
    from monolithic.model.order import Order
    from monolithic.model.payment import Payment
    from monolithic.model.user import User

    try:
        Base = declarative_base()
        Base.metadata.create_all(bind=fx_engine)
        return True

    except Exception as e:
        return False


def test_tables(fx_tables):
    assert fx_tables is not False


def test_t1(fx_user):
    assert fx_user is not None


def test_t2(fx_inventory):
    assert fx_inventory is not None


def test_t3(fx_inventory):
    assert fx_inventory is not None


def test_t4(fx_inventory):
    assert fx_inventory is not None


def test_t5(fx_inventory):
    assert fx_inventory is not None


def test_t6(fx_inventory):
    assert fx_inventory is not None


def test_t7(fx_inventory):
    assert fx_inventory is not None
