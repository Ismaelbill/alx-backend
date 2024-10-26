#!/usr/bin/env python3
""" 1. Simple pagination """


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """index_range - returns a tuple of start index and an end index
    corresponding to the range of indexes """
    return (((page - 1) * page_size), (page_size * page))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page - returns the appropriate page of the datase,
        if out of range empty list is returned"""
        assert type(page_size) == int and type(page) == int
        assert page_size > 0 and page > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start > len(dataset):
            return []
        return dataset[start:end]
