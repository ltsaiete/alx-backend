#!/usr/bin/env python3

"""
This is a simple module and it only has
one function called index_range
"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): _description_
        page_size (int): _description_

    Returns:
        Tuple[int, int]: _description_
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """_summary_
        """
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
        """return the appropriate page of the dataset
        (i.e. the correct list of rows)

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        start_row_index, end_row_index = index_range(page, page_size)

        page_lines = self.dataset()[start_row_index:end_row_index]

        return page_lines

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if total_pages > page else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
