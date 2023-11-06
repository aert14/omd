import math


def idf_transform(count_matrix: list[list[int]]) -> list[int]:
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

if __name__ == "__main__":
    count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    print(idf_transform(count_matrix))