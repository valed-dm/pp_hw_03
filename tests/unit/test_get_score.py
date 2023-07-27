"""Test for scoring function"""

import pytest

from helpers.calculate_score import calculate_score
from helpers.get_score import get_score

score_data = [
    (79789445115, None, None, None, None, None, 1.5),
    (79789445115, "dmvaled@gmail.com", None, None, None, None, 3.0),
    (79789445115, "dmvaled@gmail.com", "25.02.1979", None, None, None, 3.0),
    (79789445115, "dmvaled@gmail.com", "25.02.1979", "1", None, None, 4.5),
    (79789445115, "dmvaled@gmail.com", "25.02.1979", "1", "dmitrii", None, 4.5),
    (
        79789445115,
        "dmvaled@gmail.com",
        "25.02.1979",
        "1",
        "dmitrii",
        "valedinskii",
        5.0,
    ),
]


@pytest.mark.parametrize(
    "phone, email, birthday, gender, first_name, last_name, expected", score_data
)
def test_get_score(phone, email, birthday, gender, first_name, last_name, expected):
    """Testing get_score (it uses cache storage)"""
    score = get_score(phone, email, birthday, gender, first_name, last_name)
    assert score == expected


@pytest.mark.parametrize(
    "phone, email, birthday, gender, first_name, last_name, expected", score_data
)
def test_calculate_score(
    phone, email, birthday, gender, first_name, last_name, expected
):
    """Testing score calculation algorithm"""

    score = calculate_score(phone, email, birthday, gender, first_name, last_name)
    assert score == expected
