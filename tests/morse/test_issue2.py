import pytest

from morse import decode


@pytest.mark.parametrize(("morse", "expected"), [
    (".-", "A"),
    ("-...", "B"),
    (".-.-.-", "."),
    (".... . .-.. .--. -- .", "HELPME"),
])
def test_decode(morse: str, expected: str):
    """Pytest for decode function."""
    assert decode(morse) == expected

if __name__ == "__main__":
    pass
