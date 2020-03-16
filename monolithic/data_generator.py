"""
    Dummy test data generator
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Saturday, March 14, 2020
    :description: Dummy test data generator using Faker package
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""

import logging
import argparse
import config as conf
from config import logger
from faker import Faker
from models import db
from models.user import User
from models.inventory import Inventory
from sqlalchemy_utc import utcnow

parser = argparse.ArgumentParser(description='Initial data generator')
parser.add_argument('--mode', default='append', help='Add initial data to the table')
args = vars(parser.parse_args())

size = conf.FAKER_LENGTH
locale = conf.FAKER_LOCALE
faker = Faker(locale)


def fake_user_generator(length, fake):
    for x in range(length):
        yield User(
            user_id='{}{}'.format(fake.user_name(), fake.random_int(0, 1000)),
            password=fake.password(),
            email='{}{}'.format(fake.random_int(0, 1000), fake.email()),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number(),
            address=fake.address(),
            date=utcnow())


def fake_inventory_generator(length, fake):
    for x in range(length):
        yield Inventory(
            item_name='{} ({})'.format(fake.word(), fake.color_name()),
            price=fake.random_int(100, 99900),
            qty=fake.random_int(0, 1000),
            date=utcnow())


def add_data():
    db.Base.metadata.create_all(bind=db.engine)
    [db.session.add(user) for user in fake_user_generator(size, faker)]
    [db.session.add(item) for item in fake_inventory_generator(size, faker)]
    db.session.commit()

    logger.info('\nDB_URI: {}'.format(conf.DB_URI))
    logger.info('SQLALCHEMY_ECHO: {}'.format(conf.SQLALCHEMY_ECHO))
    logger.info('\nFaker({}) object was initiated: completed'.format(locale))
    logger.info('{} fake data added each User and Inventory tables: completed'.format(size))


try:
    if args['mode'] == 'append':
        """ Default operation """
        add_data()

    if args['mode'] == 'new':
        """ Drop the tables and add dummy data """
        db.Base.metadata.drop_all(bind=db.engine)
        add_data()

    if args['mode'] == 'drop':
        """ Drop the tables """
        db.Base.metadata.drop_all(bind=db.engine)
        logger.info('All tables are dropped.')


except Exception as e:
    logger.error(e)