#!/usr/bin/env python3
"""Async comprehension with Python"""
import asyncio
import random
from typing import Any


async def async_generator() -> Any:
    """async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
