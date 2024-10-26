#!/usr/bin/env python3
""" Simple helper function """


import typing


def index_range(page: int, page_size: int) -> typing.Tuple:
    """index_range - returns a tuple of start index and an end index
    corresponding to the range of indexes """
    return (((page - 1) * page_size), (page_size * page))
