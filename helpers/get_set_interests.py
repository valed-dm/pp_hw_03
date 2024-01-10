"""Imitates API response for get_interests request"""

import json
import random

from cache.store import store_get, cache_set


def get_interests(cid):
    """Returns list of client's preferences from imitated db storage"""

    res = store_get(f"i:{cid}")
    # return else [""] imitates client exists and db OK
    # Stupnikov's else [] -> else[""] to modify test_ok_interests_request behaviour
    return json.loads(res) if res else [""]


def set_interests(cid):
    """Sets client's preferences list in a random manner since the action is not specified"""

    key = f"i:{cid}"

    interests = [
        "cars",
        "pets",
        "travel",
        "hi-tech",
        "sport",
        "music",
        "books",
        "tv",
        "cinema",
        "geek",
        "otus",
    ]
    client_interests = json.dumps(random.sample(interests, 2))

    cache_set(key=key, expire=60 * 60, value=client_interests)
