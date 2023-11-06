import pytest
from one_hot_encoder import fit_transform


def test_fit_transform_not_none():
    """Test case when fit_transform returns not None."""
    categories = ["Moscow", "New York", "London"]
    result = fit_transform(categories)
    assert result is not None

def test_fit_transform_type():
    """Test case when fit_transform returns list."""
    categories = ["Moscow", "New York", "London"]
    result = fit_transform(categories)
    assert isinstance(result, list)

def test_fit_transform_single_category():
    """Test case with single category."""
    categories = ["Moscow"]
    expected_result = [("Moscow", [1])]
    assert fit_transform(categories) == expected_result

def test_fit_transform_duplicate_categories():
    """Test case with duplicate categories."""
    categories = ["Moscow", "Moscow"]
    expected_result = [("Moscow", [1]), ("Moscow", [1])]
    assert fit_transform(categories) == expected_result

def test_fit_transform():
    """Test case with multiply categories."""
    cities = ["Moscow", "New York", "Moscow", "London"]
    expected_result = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]
    assert fit_transform(cities) == expected_result

def test_fit_transform_no_categories():
    """Test case when no categories are provided."""
    with pytest.raises(TypeError):
        fit_transform()

if __name__ == "__main__":
    pass
