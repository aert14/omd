class CountVectorizer():
    """Преобразование текста в матрицу количества лексем."""


    def fit_transform(self: "CountVectorizer", corpus: list[str]) -> list[list[int]]:
        """Возвращает матрицу количестве лексем, полученную из корпуса."""

        # по аналогии с sklearn храним данные только текущего корпуса
        self.sent_list = [] # для хранения словарей с токенами предложений

        for sent_indx, sentence in enumerate(corpus):
            self.sent_list.append({})

            if sent_indx != 0: # добавляет в словарь предыдущие токены
                self.sent_list[sent_indx] = \
                                {i:0 for i in self.sent_list[sent_indx - 1]}

            for word in sentence.split(" "):
                word_ = word.lower()
                if word_ not in self.sent_list[sent_indx]:
                    self.sent_list[sent_indx][word_] = 1 # добавление токена
                else:
                    self.sent_list[sent_indx][word_] += 1

        # так как токены добавлялись при обработке каждого предложения
        # последовательно, необходимо добавить в словари каждого предложения,
        # исключая последнее, неучтённые токены(так как после последнего
        # токены не добавлялись). Причём очевидно, что все такие токены
        # должны быть с нулевыми значениями частоты появления.
        for sent_indx in range(len(self.sent_list) - 2, -1, -1):
            diff = {k : 0 for k in set(self.sent_list[sent_indx + 1]) - \
                                    set(self.sent_list[sent_indx ])}
            self.sent_list[sent_indx] = self.sent_list[sent_indx] | diff
        return self.count_matrix


    @property
    def feature_names(self: "CountVectorizer") -> list[str]:
        """Возвращает имена фичей."""
        return list(self.sent_list[0].keys())


    @property
    def count_matrix(self: "CountVectorizer") -> list[list[int]]:
        """Возвращает матрицу количества лексем."""
        return [list(i.values()) for i in self.sent_list]


    def get_feature_names(self: "CountVectorizer") -> list[str]:
        """Выдаёт имена фичей."""
        return self.feature_names
