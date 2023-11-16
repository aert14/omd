class CountVectorizer():
    """Преобразование текста в матрицу количества лексем."""
    def __init__(self):
        self.sent_list = []  # для хранения словарей с токенами предложений

    def fit_transform(self: "CountVectorizer", corpus: list[str]) -> list[list[int]]:
        """Возвращает матрицу количестве лексем, полученную из корпуса."""
        # по аналогии с sklearn храним данные только текущего корпуса
        self.sent_list = [] # опустошаем список словарей с токенами предложений

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

        # Итерация по sent_list в обратном порядке
        for sent_indx in range(len(self.sent_list) - 2, -1, -1):
            # Получение следующего и текущего элементов
            next_set = set(self.sent_list[sent_indx + 1])
            current_set = set(self.sent_list[sent_indx])

            # Вычисление разницы между следующим и текущим наборами
            diff = {k: 0 for k in next_set - current_set}

            # Обновление текущего набора разницей
            self.sent_list[sent_indx].update(diff)
        return self.count_matrix


    @property
    def feature_names(self: "CountVectorizer") -> list[str]:
        """Возвращает имена фичей."""
        if len(self.sent_list) == 0:
            return []
        return list(self.sent_list[-1].keys())


    @property
    def count_matrix(self: "CountVectorizer") -> list[list[int]]:
        """Возвращает матрицу количества лексем."""
        return [list(i.values()) for i in self.sent_list]


    def get_feature_names(self: "CountVectorizer") -> list[str]:
        """Выдаёт имена фичей."""
        return self.feature_names

if __name__ == "__main__":
    cv = CountVectorizer()
    corpus = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste"]

    cv.fit_transform(corpus)
    print(cv.count_matrix)
    print(cv.get_feature_names())