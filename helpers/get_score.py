"""Scores API request"""
import hashlib

from cache.store import cache_get, cache_set
from helpers.calculate_score import calculate_score


def get_score(
    phone, email, birthday=None, gender=None, first_name=None, last_name=None
):
    """Scoring calculations for non-empty request fields"""

    key_parts = [
        first_name or "",
        last_name or "",
        str(phone) or "",
        email or "",
        birthday if birthday is not None else "",
        str(gender) or "",
    ]
    key = "uid:" + hashlib.md5("".join(key_parts).encode(encoding="utf-8")).hexdigest()

    # try get from cache,
    # fallback to heavy calculation in case of cache miss
    score = cache_get(key)
    if score:
        # print("score from cache ===>", score)
        return score

    score = calculate_score(phone, email, birthday, gender, first_name, last_name)

    # cache for 60 minutes
    cache_set(key=key, expire=60 * 60, value=score)

    return score
