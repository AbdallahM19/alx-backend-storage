#!/usr/bin/env python3
"""
Web caching with Redis
"""


import redis
import requests
from functools import wraps


redis_client = redis.Redis()


def cache_data(method):
    """Cache data in Redis"""
    @wraps(method)
    def wrap_url(url):
        """Wrap the url to cache it in Redis"""
        res = redis_client.get('cached:{}'.format(url))
        if res:
            return res.decode('utf-8')
        res = method(url)
        redis_client.incr('count:{}'.format(url))
        redis_client.set('count:{}'.format(url), res, ex=10)
        redis_client.expire('result:{}'.format(url), 10)
        return res
    return wrap_url


@cache_data
def get_page(url: str) -> str:
    """Get page from url"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
