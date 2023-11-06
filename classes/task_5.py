from task_1 import CountVectorizer
from task_4 import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    """TfidfVectorizer class."""

    def __init__(self) -> None:
        super().__init__()
        self.tfidf_matrix = []

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """Fit and transform corpus."""
        count_matrix = super().fit_transform(corpus)
        print(count_matrix)
        tf_idf = TfidfTransformer()
        self.tfidf_matrix = tf_idf.fit_transform(count_matrix)
        return self.tfidf_matrix

if __name__ == "__main__":
    corpus = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste"]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
