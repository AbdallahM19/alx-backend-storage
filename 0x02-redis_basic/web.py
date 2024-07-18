#!/usr/bin/env python3
"""
Web caching with Redis
"""


import redis
import requests
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def cache_data(method: Callable) -> Callable:
    """Cache data in Redis"""
    @wraps(method)
    def wrap_url(url) -> str:
        """Wrap the url to cache it in Redis"""
        redis_client.incr('count:{}'.format(url))
        res = redis_client.get('result:{}'.format(url))
        if res:
            return res.decode('utf-8')
        res = method(url)
        redis_client.set('count:{}'.format(url), 0)
        redis_client.setex('result:{}'.format(url), 10, res)
        return res
    return wrap_url


@cache_data
def get_page(url: str) -> str:
    """Get page from url"""
    response = requests.get(url)
    return response.text
