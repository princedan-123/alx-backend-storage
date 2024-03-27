#!/usr/bin/env python3
"""A python script that creates a cache using redis."""
from typing import Union
from typing import Callable, Any
import redis
import uuid


class Cache:
    """A class that uses the Redis Class to create a cache."""
    def __init__(self):
        """Initialization method of the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """An instance method that stores data to redis instance."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Any = None) -> Union[bytes, Any]:
        """An instance method that retreives data from redis."""
        if fn is not None:
            data = self._redis.get(key)
            if data is not None:
                return fn(data)
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """An instance method that converts retrieved data to string."""
        return self.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """An instance method that converts a retrieved data to integer."""
        return int.from_bytes(self.get(key), byteorder='big')
