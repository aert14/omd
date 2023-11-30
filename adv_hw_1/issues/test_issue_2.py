import json

from solution_issue_2 import Advert


def test_color():
    """Test for color."""
    json_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
        }"""
    advert = Advert(json.loads(json_str))
    assert advert.__str__().startswith("\033[33m") is True


def test_stick():
    """Test for stick."""
    json_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
        }"""
    advert = Advert(json.loads(json_str))
    expected = "\033[33mВельш-корги | 1000₽\033[0m"
    assert str(advert) == expected


if __name__ == "__main__":
    test_color()
    test_stick()
