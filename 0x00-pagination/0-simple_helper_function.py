#!/usr/bin/env python3

"""
This is a simple module and it only has
one function called index_range
"""

from typing import Tuple

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
