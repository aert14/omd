import contextlib
import json

import pytest
from solution_issue_1 import Advert


def test_lesson():
    """Test for lesson."""
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    assert lesson_ad.price == 0


def test_dog():
    """Test for dog."""
    dog_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    expected = ["dogs", 1000]
    assert dog_ad.class_ == expected[0]
    assert dog_ad.price == expected[1]


def test_negative_price_1():
    """Test for negative price."""
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)

    with contextlib.suppress(ValueError):
        Advert(lesson)


def test_negative_price_2():
    """Test for negative price."""
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    with contextlib.suppress(ValueError):
        lesson_ad.price = -3


def test_not_set_price():
    """Test for not set price."""
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0


def test_advert_missing_title():
    """Test for advert missing title."""
    with pytest.raises(ValueError, match="Missing 'title' attribute"):
        Advert({})
