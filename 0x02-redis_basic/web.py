#!/usr/bin/env python3
"""Web caching with Redis"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def cache_data(method: Callable) -> Callable:
    """Cache data in Redis"""
    @wraps(method)
    def wrap_url(url: str) -> str:
        """Wrap the url to cache it in Redis"""
        redis_client.incr('count:{}'.format(url))
        result = redis_client.get('result:{}'.format(url))
        if result:
            return result.decode('utf-8')
        res = method(url)
        redis_client.setex('result:{}'.format(url), 10, result)
        return res
    return wrap_url


@cache_data
def get_page(url: str) -> str:
    """Get page from url"""
    response = requests.get(url)
    return response.text
