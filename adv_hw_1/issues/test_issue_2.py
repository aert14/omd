from solution_issue_2 import Advert
import json


def test_color():
    json_str =  """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
        }"""
    advert = Advert(json.loads(json_str))
    assert advert.__str__().startswith('\033[33m') == True

def test_stick():
    json_str =  """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
        }"""
    advert = Advert(json.loads(json_str))
    assert str(advert) == "\033[33mВельш-корги | 1000₽\033[0m"
