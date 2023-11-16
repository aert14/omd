import pytest
from task_3 import idf_transform


def test_count_matrix():
    """Test count matrix."""
    count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    expected_res =  [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]

    assert idf_transform(count_matrix) == expected_res

def test_one_line_count_matrix():
    """Test one line count matrix."""
    count_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    expected_res =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    assert idf_transform(count_matrix) == expected_res


def test_empty_matrix():
    """Test empty matrix."""
    count_matrix = []
    assert idf_transform(count_matrix) == []

def test_invalid_input():
    """Test invalid input."""
    count_matrix = "123"
    with pytest.raises(TypeError):
        idf_transform(count_matrix)

if __name__ == "__main__":
    pass
