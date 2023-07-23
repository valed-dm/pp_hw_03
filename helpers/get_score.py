"""Scores API request"""
import hashlib

from cache.store import cache_get, cache_set


def get_score(
    phone, email, birthday=None, gender=None, first_name=None, last_name=None
):
    """Scoring calculations for non-empty request fields"""

    key_parts = [
        first_name or "",
        last_name or "",
        str(phone) or "",
        birthday if birthday is not None else "",
    ]
    key = "uid:" + hashlib.md5("".join(key_parts).encode(encoding="utf-8")).hexdigest()

    # try get from cache,
    # fallback to heavy calculation in case of cache miss
    score = cache_get(key) or 0

    if score:
        # print("score from cache ===>", score)
        return score

    if phone:
        score += 1.5
    if email:
        score += 1.5
    if birthday and gender is not None:
        score += 1.5
    if first_name and last_name:
        score += 0.5

    # cache for 60 minutes
    cache_set(key=key, expire=60 * 60, value=score)

    return score
