"""Test for Redis data storage"""

import json
import uuid

import pytest
import redis

from cache.store import cache_set, cache_get, store_get, r_connect

value_data = [
    ("sc:" + uuid.uuid4().hex, 60 * 60, 5.0, 5.0),
    (
        "i:" + uuid.uuid4().hex,
        60 * 60,
        json.dumps(["sports", "geek"]),
        ["sports", "geek"],
    ),
]


@pytest.mark.parametrize("key, expire, value, expected", value_data)
class TestStore:
    """Tests redis storage"""

    def test_store(self, key, expire, value, expected):
        """Testing cache(cache_get), imitated db(store_get)"""

        try:
            # check if redis connection is alive
            r = redis.Redis()

            if r.ping():
                if key.startswith("sc:"):
                    cache_set(key, expire, value)
                    score = cache_get(key)
                    assert float(score) == expected
                elif key.startswith("i:"):
                    cache_set(key, expire, value)
                    interests = store_get(key)
                    assert json.loads(interests) == expected

        except redis.ConnectionError:
            score = cache_get(key)
            assert score is None
            interests = store_get(key)
            assert json.loads(interests) == [
                "Unable to get client_interests: db connection lost"
            ]


class TestRedisConnect:
    """Tests redis connection attempts"""

    count = 0

    def counter(self):
        """Counts redis connection attempts qty"""
        self.count += 1

    def test_redis_connect(self):
        """Redis connection max_retries qty attempts testing"""

        try:
            r_connect(self.counter)
        except redis.ConnectionError:
            # max_retries = 5
            assert self.count == 5

        assert self.count == 1
