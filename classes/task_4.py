import math


class TfidfTransformer:
    """TF-IDF transformer class."""

    def __init__(self) -> None:
        self.tf = []
        self.idf = []
        self.tf_idf = []

    def tf_transform(self, count_matrix: list[list[int]]) -> list[list[int]]:
        """TF transform of the count_matrix."""
        if not isinstance(count_matrix, list):
            msg = "count_matrix must be a list"
            raise TypeError(msg)

        sums = [sum(i) for i in count_matrix]

        return [[round(i / sums[j],3) for i in count_matrix[j]] for\
                    j in range(len(count_matrix))]

    def idf_transform(self, count_matrix: list[list[int]]) -> list[list[int]]:
        """IDF transform of the count_matrix."""
        if not isinstance(count_matrix, list):
            msg = "count_matrix must be a list"
            raise TypeError(msg)

        if len(count_matrix) == 0:
            return []

        idfs = []
        total_docs = len(count_matrix)

        total_words = len(count_matrix[0])
        for i in range(total_words):
            docs_i = 0
            for doc in count_matrix:
                if doc[i] > 0:
                    docs_i += 1
            idfs.append(round(math.log((total_docs + 1)/(docs_i + 1)) + 1, 1))
        return idfs

    def tf_idf_transform(self, count_matrix: list[list[int]]) -> list[list[int]]:
        """TF-IDF transform of the count_matrix."""
        self.idf = self.idf_transform(count_matrix)
        self.tf = self.tf_transform(count_matrix)
        res = []
        for doc in self.tf:
            res.append([round(t * i,3) for t, i in zip(doc, self.idf)])
        return res

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[int]]:
        """Fit and transform count_matrix."""
        self.tf_idf = self.tf_idf_transform(count_matrix)
        return self.tf_idf

if __name__ == "__main__":
    count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
