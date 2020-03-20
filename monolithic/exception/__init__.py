"""
    BaseException for transaction test
    ~~~~~~~~~~~~~~~~~~~~~~~

    :created date: Thursday, March 19, 2020
    :description: BaseException for transaction test
    :copyright: © 2020 written by sungshik (liks79@gmail.com)
    :license: BSD 3-Clause License, see LICENSE for more details.
"""


class Error(Exception):
    pass


class OutOfStockError(Error):
    pass


class PaymentFailureError(Error):
    pass
