import pytest
from task_5 import TfidfVectorizer


def test_feature_names():
    """Test feature names."""
    corpus = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste"]
    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(corpus)
    expected =  ["crock", "pot", "pasta", "never", "boil", "again", "pomodoro",
                 "fresh", "ingredients", "parmesan", "to", "taste"]
    assert vectorizer.get_feature_names() == expected

def test_tdidf_matrix():
    """Test td_idf matrix."""
    corpus = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste"]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    expected = [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
    assert tfidf_matrix == expected

if __name__ == "__main__":
    pass
