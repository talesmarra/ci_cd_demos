"""
Define operations
"""
from typing import Union

Number = Union[int, float]

def add(first: Number, second: Number) -> Number:
    """
    :param first: first number to be summed
    :param second: second number to be summed
    :return: sum
    """
    return first + second

def subtract(first: Number, second: Number) -> Number:
    """
    :param first: first number
    :param second: second number
    :return: difference (first - second)
    """
    return first - second

def multiply(first: Number, second: Number) -> Number:
    """
    :param first: first number
    :param second: second number
    :return: product (first * second)
    """
    # this is a special case because 'c' * 2 gives 'cc' in python which
    # is not what we want
    if not (isinstance(first, float) and isinstance(second, float)):
        try:
            first = float(first)
        except TypeError as exc:
            raise TypeError('Numbers should be float') from exc
    return first * second

def divide(first: Number, second: Number) -> Number:
    """
    :param first: first number
    :param second: second number
    :return: division (first / second)
    """
    return first / second
