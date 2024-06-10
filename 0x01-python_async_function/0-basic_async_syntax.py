#!/usr/bin/env python3
"""Async with Python"""
import random
import asyncio


async def wait_random(max_delay: int = 10):
    """
    waits for a random delay between 0 and max_delay
    """
    wait_time = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(wait_time)
    return wait_time
