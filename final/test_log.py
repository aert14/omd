from logs import log


class TestClass:
    """Test class."""

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
    """Test bake log."""
    test_obj = TestClass()
    test_obj.bake()
    captured = capsys.readouterr()
    assert "🍳Приготовили" in captured.out

def test_deliver_log(capsys):
    """Test deliver log."""
    test_obj = TestClass()
    test_obj.deliver()
    captured = capsys.readouterr()
    assert "🛵Доставили" in captured.out

def test_pickup_log(capsys):
    """Test pickup log."""
    test_obj = TestClass()
    test_obj.pickup()
    captured = capsys.readouterr()
    assert "🏡Забрали" in captured.out
if __name__ == "__main__":
    pass
