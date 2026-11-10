from datetime import date

from age_logic import calculate_age, next_birthday, zodiac_sign
from ml_model import predict_remaining_years


def test_basic_age():
    age = calculate_age(date(2000, 1, 15), date(2025, 3, 20))
    assert (age["years"], age["months"], age["days"]) == (25, 2, 5)


def test_day_borrow():
    age = calculate_age(date(2000, 1, 31), date(2025, 3, 1))
    assert age["years"] == 25 and age["months"] == 1


def test_next_birthday_today_is_zero():
    assert next_birthday(date(2000, 5, 5), date(2025, 5, 5))["days_left"] == 0


def test_zodiac():
    assert zodiac_sign(date(2000, 3, 25)) == "Aries"
    assert zodiac_sign(date(2000, 1, 5)) == "Capricorn"


def test_ml_decreases_with_age():
    assert predict_remaining_years(20) > predict_remaining_years(60) > 0
