#!/usr/bin/env python3
"""
Cache class
"""


import redis
from uuid import uuid4
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[
        str, bytes, int, float]:
        """get data from cache"""
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        automatically parametrize Cache.get
        get data from cache
        """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        automatically parametrize Cache.get
        get data from cache
        """
        return self.get(key, lambda x: int(x))
