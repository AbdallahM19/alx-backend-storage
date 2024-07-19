#!/usr/bin/env python3
"""Web caching with Redis"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_client = redis.Redis()
"""The module-level Redis instance."""


def data_cacher(method: Callable) -> Callable:
    """Cache data in Redis"""
    @wraps(method)
    def wrap_url(url) -> str:
        """Wrap the url to cache it in Redis"""
        redis_client.incr('count:{}'.format(url))
        result = redis_client.get('result:{}'.format(url))
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_client.set('count:{}'.format(url), 0)
        redis_client.setex('result:{}'.format(url), 10, result)
        return result
    return wrap_url


@data_cacher
def get_page(url: str) -> str:
    """Get page from url"""
    return requests.get(url).text
