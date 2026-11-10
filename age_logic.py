"""Pure-Python age calculation helpers (no Flask here, so they are easy to test)."""
from datetime import date

ZODIAC = [  # (month, day) where the sign STARTS
    ((1, 20), "Aquarius"), ((2, 19), "Pisces"), ((3, 21), "Aries"),
    ((4, 20), "Taurus"), ((5, 21), "Gemini"), ((6, 21), "Cancer"),
    ((7, 23), "Leo"), ((8, 23), "Virgo"), ((9, 23), "Libra"),
    ((10, 23), "Scorpio"), ((11, 22), "Sagittarius"), ((12, 22), "Capricorn"),
]


def calculate_age(birth: date, today: date) -> dict:
    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day
    if days < 0:
        months -= 1
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days += days_in_month(prev_year, prev_month)
    if months < 0:
        years -= 1
        months += 12
    return {"years": years, "months": months, "days": days,
            "total_days": (today - birth).days}


def days_in_month(year: int, month: int) -> int:
    if month == 12:
        return 31
    return (date(year, month + 1, 1) - date(year, month, 1)).days


def next_birthday(birth: date, today: date) -> dict:
    try:
        nxt = birth.replace(year=today.year)
    except ValueError:  # born on 29 Feb
        nxt = date(today.year, 3, 1)
    if nxt < today:
        try:
            nxt = birth.replace(year=today.year + 1)
        except ValueError:
            nxt = date(today.year + 1, 3, 1)
    return {"date": nxt.isoformat(), "days_left": (nxt - today).days,
            "weekday": nxt.strftime("%A")}


def zodiac_sign(birth: date) -> str:
    sign = "Capricorn"
    for (month, day), name in ZODIAC:
        if (birth.month, birth.day) >= (month, day):
            sign = name
    if (birth.month, birth.day) < (1, 20):
        sign = "Capricorn"
    return sign


def generation(year: int) -> str:
    if year >= 2013: return "Gen Alpha"
    if year >= 1997: return "Gen Z"
    if year >= 1981: return "Millennial"
    if year >= 1965: return "Gen X"
    if year >= 1946: return "Baby Boomer"
    return "Silent Generation"
