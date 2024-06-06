#!/usr/bin/env python3
"""Annotations"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats
    Args:
        input_list (list): A list of floats
    Returns:
        float: The sum of the floats in the list
    """
    if input_list:
        return sum(input_list)
    else:
        return 0.0
