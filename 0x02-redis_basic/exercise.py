#!/usr/bin/env python3
"""A python script that creates a cache using redis."""
import typing
import redis
import uuid


class Cache:
    """A class that uses the Redis Class to create a cache."""
    def __init__(self):
        """Initialization method of the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, int, float]) -> str:
        """An instance method that stores data to redis instance."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
