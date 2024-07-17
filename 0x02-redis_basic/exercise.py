#!/usr/bin/env python3
"""
Cache class
"""


import redis
from uuid import uuid4
from typing import Union, Any


class Cache:
    """class cache"""
    def __init__(self) -> None:
        """initializes instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in cache"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
