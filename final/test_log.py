import pytest
from logs import log

class TestClass:

    size = "L"

    @log("🍳Приготовили за {}c")
    def bake(self) -> None:
        """Готовит пиццу."""

    @log("🛵Доставили за {}c")
    def deliver(self) -> None:
        """Доставляет пиццу."""

    @log("🏡Забрали за {}c")
    def pickup(self) -> None:
        """Самовывозит пиццу."""

def test_bake_log(capsys):
    test_obj = TestClass()
    test_obj.bake()
    captured = capsys.readouterr()
    assert "🍳Приготовили" in captured.out

def test_deliver_log(capsys):
    test_obj = TestClass()
    test_obj.deliver()
    captured = capsys.readouterr()
    assert "🛵Доставили" in captured.out

def test_pickup_log(capsys):
    test_obj = TestClass()
    test_obj.pickup()
    captured = capsys.readouterr()
    assert "🏡Забрали" in captured.out
