class CountVectorizer():
    """Преобразование текста в матрицу количества лексем."""

    def __init__(self: "CountVectorizer") -> None:
        """Конструктор класса CountVectorizer."""
        self.sent_list = []

    def fit_transform(self: "CountVectorizer", corpus: list[str]) -> list[int]:
        """Возвращает матрицу количестве лексем, полученную из корпуса."""
        for sent_indx, sentence in enumerate(corpus):
            self.sent_list.append({})

            if sent_indx != 0: # добавляет в словарь предыдущие токены
                self.sent_list[sent_indx] = \
                                {i:0 for i in self.sent_list[sent_indx - 1]}


            for word in sentence.split(" "):
                word_ = word.lower()
                if word_ not in self.sent_list[sent_indx]:
                    self.sent_list[sent_indx-1][word_] = 0 # для формата
                    self.sent_list[sent_indx][word_] = 1
                else:
                    self.sent_list[sent_indx][word_] += 1
        return self.count_matrix
    @property
    def feature_names(self: "CountVectorizer") -> list[str]:
        """Возвращает имена фичей."""
        return list(self.sent_list[0].keys())
    @property
    def count_matrix(self: "CountVectorizer") -> list[list[int]]:
        """Возвращает матрицу количества лекцем."""
        return [list(i.values()) for i in self.sent_list]

    def get_feature_names(self: "CountVectorizer") -> list[str]:
        """Выдаёт имена фичей."""
        return self.feature_names
