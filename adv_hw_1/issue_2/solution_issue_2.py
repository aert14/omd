import sys

sys.path.append("issue_1")

import json

from issue_1.solution_issue_1 import Advert


class ColorizeMixin:
    """Colorize mixin for Advert class."""

    repr_color_code = 32

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Установка repr_color_code по умолчанию, если он не определен в подклассе
        if "repr_color_code" not in cls.__dict__:
            cls.repr_color_code = ColorizeMixin.repr_color_code

    def __str__(self):
        return f"\033[{self.repr_color_code}m{self.title} | {self.price}₽\033[0m"

class Advert(ColorizeMixin, Advert):
    """Modified Advert class."""

    repr_color_code = 33

if __name__ == "__main__":
    json_str = '{"title":"Вельш-корги", "price":1000, "class":"dogs",\
                 "location": {"address":"Тестовый адрес"}}'
    advert = Advert(json.loads(json_str))

    print(advert)  # Вывод с цветовым оформлением
    print(advert.location.address)  # Доступ к вложенному атрибуту
    print(advert.class_)  # Доступ к атрибуту, являющемуся ключевым словом
