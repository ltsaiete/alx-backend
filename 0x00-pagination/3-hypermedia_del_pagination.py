#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """_summary_

        Args:
            index (int, optional): _description_. Defaults to None.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            Dict: _description_
        """
        dataset = self.indexed_dataset()
        data = []
        next_index = index + page_size

        assert index <= len(dataset)

        for idx in range(index, next_index):
            if idx not in dataset:
                
                next_index = next_index + 1

                continue
            data.append(dataset[idx])

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }


