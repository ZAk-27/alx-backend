#!/usr/bin/env python3
""" documentation style """
import csv
import math
from typing import List, Tuple


class Server:
    """documentation style."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ documentation style"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ documentation style"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """documentation style"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """documentation style"""
        startPage = (page - 1) * page_size
        endPage = page * page_size
        return (startPage, endPage)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """documentation style"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
