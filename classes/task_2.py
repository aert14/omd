def tf_transform(count_matrix: list[list[int]]) -> list[list[int]]:
    """TF transform of the count_matrix."""
    if not isinstance(count_matrix, list):
        msg = "count_matrix must be a list"
        raise TypeError(msg)

    sums = [sum(i) for i in count_matrix]

    return [[round(i / sums[j],3) for i in count_matrix[j]] for\
             j in range(len(count_matrix))]

if __name__ == "__main__":
    count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    print(tf_transform(count_matrix))
