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
        """method that takes the same arguments
        (and defaults) as get_page and returns a dict """
        start, end = index_range(page, page_size)
        get_page: List[List] = self.get_page(page, page_size)
        obj: Dict = {}
        obj['page_size'] = len(get_page)
        obj['page'] = page
        obj['data'] = get_page
        obj['next_page'] = page + 1 if end < len(self.__dataset) else None
        obj['prev_page'] = page - 1 if start > 0 else None
        obj['total_pages'] = math.ceil(len(self.__dataset) / page_size)
        return obj
