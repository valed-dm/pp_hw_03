"""Imitates API response for get_interests request"""

import random


def get_interests(store, cid):
    """Returns randon values"""

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
        "otus"
    ]
    return random.sample(interests, 2)
