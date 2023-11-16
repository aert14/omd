import pytest
from task_1 import CountVectorizer


def test_feature_names():
    """Test feature names."""
    cv = CountVectorizer()
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    cv.fit_transform(corpus)
    expected = ["crock", "pot", "pasta", "never", "boil", "again", \
                "pomodoro", "fresh", "ingredients", "parmesan", "to",\
                "taste"]
    assert cv.feature_names == expected

def test_count_matrix():
    """Test count matrix."""
    cv = CountVectorizer()
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"
    ]
    cv.fit_transform(corpus)
    assert cv.count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
                               [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

def test_empty_corpus():
    """Test empty corpus."""
    cv = CountVectorizer()
    corpus = []
    cv.fit_transform(corpus)
    assert cv.feature_names == []
    assert cv.count_matrix == []

def test_invalid_input():
    """Test invalid input."""
    cv = CountVectorizer()
    with pytest.raises(TypeError):
        cv.fit_transform(123)

if __name__ == "__main__":
    pass
