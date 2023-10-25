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
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        start_row_index, end_row_index = index_range(page, page_size)
        page_lines = []

        with open(self.DATA_FILE, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)

            for _ in range(start_row_index):
                try:
                    next(csv_reader)
                except StopIteration:
                    return []

            for current_row_index, row in enumerate(csv_reader):
                page_lines.append(row)
                if current_row_index >= end_row_index - 1:
                    break

        return page_lines
