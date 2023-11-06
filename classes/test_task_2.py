import pytest
from task_2 import tf_transform


def test_count_matrix():
    """Test count matrix."""
    count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    expected_res = [[0.143, 0.143, 0.286, 0.143, 0.143, 0.143, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0.143, 0, 0, 0, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143]]

    assert tf_transform(count_matrix) == expected_res

def test_one_line_count_matrix():
    """Test one line count matrix."""
    count_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    expected_res =  [[0.083] * len(count_matrix[0])]

    assert tf_transform(count_matrix) == expected_res

def test_empty_matrix():
    """Test empty matrix."""
    count_matrix = []
    assert tf_transform(count_matrix) == []

def test_invalid_input():
    """Test invalid input."""
    count_matrix = "123"
    with pytest.raises(TypeError):
        tf_transform(count_matrix)

if __name__ == "__main__":
    pass
