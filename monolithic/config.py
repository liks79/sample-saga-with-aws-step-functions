"""
    Configuration variables from OS environment
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Thursday, March 12, 2020
    :description: Configuration variables for monolithic application
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""

import os
import sys
import time
import logging

# Configuration variables from OS environment
DB_URI = os.getenv('TEST_DB_URI', 'sqlite:////tmp/sqlite.test.db')
SQLALCHEMY_ECHO = eval(os.getenv('SQLALCHEMY_ECHO', 'False'))
LOGGER_NAME = os.getenv('MONOLITHIC_LOGGER', 'MONOLITHIC')
LOG_LEVEL = os.getenv('MONOLITHIC_LOG_LEVEL', logging.DEBUG)
FAKER_LOCALE = os.getenv('FAKER_LOCALE', 'en_US')
FAKER_LENGTH = int(os.getenv('FAKER_LENGTH', '100'))

# Logger initialize
logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(LOG_LEVEL)
log_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
log_handler.setFormatter(formatter)
logging.Formatter.converter = time.gmtime
logger.addHandler(log_handler)


