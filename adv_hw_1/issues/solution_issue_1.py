import json
import keyword


class Advert:
    """Class for processing the json of advert."""

    def __init__(self, mapping: dict, is_top_level: bool = True):
        for key, value in mapping.items():
            if isinstance(value, dict):
                # Создаем вложенный Advert без проверки title
                value = Advert(value, is_top_level=False)

            setattr(self, key, value)

        if is_top_level and not hasattr(self, "title"):
            msg = "Missing 'title' attribute"
            raise ValueError(msg)

    @property
    def price(self) -> int:
        """Get price of advert."""
        if not hasattr(self, "_price"):
            self._price = 0
        return self._price

    @price.setter
    def price(self, value) -> None:
        """Set price of advert."""
        if value < 0:
            msg = "price must be >= 0"
            raise ValueError(msg)
        self._price = value

    def __setattr__(self, __name: str, __value: any) -> None:
        """Modify setattr for processing keywords."""
        if keyword.iskeyword(__name):
            __name += "_"
        super().__setattr__(__name, __value)


if __name__ == "__main__":
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
    print(lesson_ad.location.address)
    print(lesson_ad.price)
