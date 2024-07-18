#!/usr/bin/env python3
"""Web caching with Redis"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Cache data in Redis"""
    @wraps(method)
    def invoker(url: str) -> str:
        """Wrap the url to cache it in Redis"""
        redis_client.incr(f'count:{url}')
        result = redis_client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_client.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Get page from url"""
    return requests.get(url).text
