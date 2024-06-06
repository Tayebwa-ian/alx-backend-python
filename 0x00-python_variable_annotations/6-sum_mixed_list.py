#!/usr/bin/env python3
"""
Annotations
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """Takes a mixed list of integers and floats and returns the
    sum of all the numbers in the list as float"""
    return sum(mxd_lst)
