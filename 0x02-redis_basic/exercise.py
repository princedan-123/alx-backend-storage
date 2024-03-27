#!/usr/bin/env python3
"""A python script that creates a cache using redis."""
from typing import Union
from typing import Callable, Any
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """A decorator that increments a key in redis."""
    @wraps(method)
    def wrapper(self, data):
        """A wrapper function that wraps the original function."""
        key = method.__qualname__
        result = method(self, data)
        self._redis.incr(key)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """A decorator that stores its input and output in redis."""
    @wraps(method)
    def wrapper(self, data):
        """A wrapper function that wraps the original function."""
        key_input = f"{method.__qualname__}:inputs"
        key_output = f"{method.__qualname__}:outputs"
        self._redis.rpush(key_input, str(data))
        result = method(self, data)
        self._redis.rpush(key_output, result)
        return result
    return wrapper


class Cache:
    """A class that uses the Redis Class to create a cache."""
    def __init__(self):
        """Initialization method of the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
        return int(self.get(key))
