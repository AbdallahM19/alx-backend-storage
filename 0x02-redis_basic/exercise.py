#!/usr/bin/env python3
"""
Cache class
"""


import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable, Any


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a function"""
    @wraps(method)
    def wrap_incr(self, *args, **kwargs) -> Any:
        """Wrap the method to count calls"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrap_incr

class Cache:
    """class cache"""
    def __init__(self) -> None:
        """initializes instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
