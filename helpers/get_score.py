"""Scores API request"""


def get_score(store, phone, email, birthday=None, gender=None, first_name=None, last_name=None):
    """Scoring calculations for non-empty request fields"""

    score = 0

    if phone:
        score += 1.5
    if email:
        score += 1.5
    if birthday and gender is not None:
        score += 1.5
    if first_name and last_name:
        score += 0.5

    return score
