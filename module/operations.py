"""
Define operations
"""
from typing import Union

number = Union[int, float]

def add(first: number, second: number) -> number:
    """
    :param first: first number to be summed
    :param second: second number to be summed
    :return: sum
    """
    return first + second

def subtract(first: number, second: number) -> number:
    """
    :param first: first number
    :param second: second number
    :return: difference (first - second)
    """
    return first - second

def multiply(first: number, second: number) -> number:
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
        except TypeError:
            raise TypeError('Numbers should be float')
    return first * second

def divide(first: number, second: number) -> number:
    """
    :param first: first number
    :param second: second number
    :return: division (first / second)
    """
    return first / second
