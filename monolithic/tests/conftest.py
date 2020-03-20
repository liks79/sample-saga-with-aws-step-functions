"""
    Fixtures for unittest
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: 3/16/20
    :description: Fixtures for unittest
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""
import config
from faker import Faker
from pytest import fixture
from model.user import User
from model.order import Order
from model.payment import Payment
from model.inventory import Inventory
from model.membership import Membership
from sqlalchemy.engine import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy_utc import utcnow

fake = Faker(config.FAKER_LOCALE)


@fixture(scope='function', params=[config.DB_URI])
def fx_engine(request):
    db_url = request.param
    engine = create_engine(db_url, poolclass=NullPool)
    return engine


@fixture(scope='function')
def fx_user():
    return User(user_id=fake.user_name(),
                password=fake.password(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                address=fake.address(),
                date=utcnow())


@fixture(scope='function')
def fx_inventory():
    return Inventory(item_name='{} ({})'.format(fake.word(), fake.color_name()),
                     price=fake.random_int(100, 99900),
                     qty=fake.random_int(0, 1000),
                     date=utcnow())


@fixture(scope='function')
def fx_payment_success(fx_user):
    return Payment(pay_type='credit_card',
                   user_id=fx_user.user_id,
                   allowed=True,
                   date=utcnow())


@fixture(scope='function')
def fx_order(fx_user, fx_inventory):
    return Order(user_id=fx_user.user_id,
                 item_id=fx_inventory.item_id,
                 item_qty=fake.random_int(1, 100),
                 date=utcnow(),
                 deliver_phone=fake.phone_number(),
                 deliver_address=fake.address(),
                 total_price=fake.random_int(100, 1000000))


@fixture(scope='function')
def fx_membership(fx_user):
    return Membership(user_id=fx_user.user_id,
                      date=utcnow(),
                      mileage=fake.random_int(10, 400))
