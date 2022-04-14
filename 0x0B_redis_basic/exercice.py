#!/usr/bin/env python3
"""
Exercise file
"""
from typing import Callable, Optional, Union
import redis
import uuid
import sys
from functools import wraps


def replay(fn):
    """ display the history of calls of a particular function """
    store = redis.Redis()
    count_key = fn.__qualname__
    input_key = count_key + ":inputs"
    output_key = count_key + ":outputs"
    count = store.get(count_key).decode("utf-8")
    print("{} was called {} times:".format(count_key, count))
    inputs = store.lrange(input_key, 0, count)
    outputs = store.lrange(output_key, 0, count)
    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print("{}(*{}) -> {}".format(count_key, input, output))


def count_calls(method: Callable) -> Callable:
    """ Calls counter decorator """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Method wrapper to incr count """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Calls call history decorator """
    key = method.__qualname__
    input_key = key + ":inputs"
    output_key = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Method wrapper to push history in store """
        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(data))
        return data
    return wrapper


class Cache:
    """ Redis cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Constructor """
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Get originaltype data """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, value: bytes) -> str:
        """ Converts bytes to string """
        return value.decode("utf-8")

    def get_int(self, value: bytes) -> str:
        """ Converts bytes to integer """
        return int.from_bytes(value, sys.byteorder)
