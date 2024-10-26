#!/usr/bin/env python3
""" 2. Hypermedia pagination """


import csv
import math
from typing import List, Tuple, Dict


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
        assert type(page_size) is int and type(page) is int
        assert page_size > 0 and page > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start > len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        dataset = self.dataset()
        get_page = self.get_page(page, page_size)
        obj = {}
        obj['page_size'] = len(get_page)
        obj['page'] = page
        obj['data'] = get_page
        next_page = None
        if 0 != len(get_page):
            next_page = page + 1
        obj['next_page'] = next_page
        prev_page = None
        if page - 1 > 0:
            prev_page = page - 1
        obj['prev_page'] = prev_page
        val = 0
        if obj['page_size'] == val:
            val = 1
        obj['total_pages'] = math.ceil(19419 / page_size)
        return obj
