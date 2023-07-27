"""Score estimate logic"""


def calculate_score(phone, email, birthday, gender, first_name, last_name):
    """Computes score value"""

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
