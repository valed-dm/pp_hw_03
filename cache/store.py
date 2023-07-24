"""Score API redis storage"""
import json
import logging
import time

import redis

r = redis.Redis()
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname).1s %(message)s",
    datefmt="%Y.%m.%d %H:%M:%S",
)


def r_connect(f, *args, **kwargs):
    """Keeps on trying to connect to redis storage max_retries times"""

    count = 0
    max_retries = 5

    while True:
        try:
            return f(*args, **kwargs)
        except redis.ConnectionError:
            count += 1
            # stops attempts if we've exceeded max_retries
            if count > max_retries:
                logging.error("redis cache unavailable")
                return None
            backoff = count * 0.1
            logging.info("Retrying redis connection in %d seconds", backoff)
            time.sleep(backoff)


def cache_set(key, expire, value):
    """Saves data to cache or imitated db"""

    # key expired in expire time
    # take care of SETEX positional args order
    r_connect(r.setex, key, expire, value)


def cache_get(key):
    """Extracts cached score (float(cached_value)) values"""

    # IT'S POSSIBLE CHECK KEY FORMAT AND RETURN DIFFERENT DATA TYPES DEPEND ON IT
    # we receive score as binary, next convert to float
    cached_value = r_connect(r.get, key)
    if cached_value:
        return float(cached_value)

    return None


def store_get(key):
    """Imitates request to db storage. Extracts imitated db values"""

    value = r_connect(r.get, key)
    if value:
        return value
    else:
        try:
            # check redis connection
            r.ping()
            return None
        # returns info message if db is unavailable at a moment
        except redis.ConnectionError:
            logging.error("db connection lost")
            return json.dumps(["Unable to get client_interests: db connection lost"])
