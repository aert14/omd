import pytest
from task_4 import TfidfTransformer


def test_count_matrix():
    """Test count matrix."""
    tf_idf = TfidfTransformer()
    count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    expected_res =   [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

    assert tf_idf.fit_transform(count_matrix) == expected_res

def test_empty_matrix():
    """Test empty matrix."""
    tf_idf = TfidfTransformer()
    count_matrix = []
    assert tf_idf.fit_transform(count_matrix) == []

def test_invalid_input():
    """Test invalid input."""
    tf_idf = TfidfTransformer()
    count_matrix = "123"
    with pytest.raises(TypeError):
        tf_idf.fit_transform(count_matrix)

if __name__ == "__main__":
    pass
