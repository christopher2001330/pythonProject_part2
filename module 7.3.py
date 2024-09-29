import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в кортеже

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Читаем содержимое файла
                content = file.read().lower()  # Переводим текст в нижний регистр
                # Удаляем пунктуацию
                content = content.translate(str.maketrans('', '', string.punctuation))
                # Разбиваем на слова
                words = content.split()
                all_words[file_name] = words  # Записываем в словарь
        return all_words

    def find(self, word):
        results = {}
        word = word.lower()  # Переводим искомое слово в нижний регистр
        all_words = self.get_all_words()  # Получаем все слова
        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1  # Сохраняем позицию первого вхождения
        return results

    def count(self, word):
        results = {}
        word = word.lower()  # Переводим искомое слово в нижний регистр
        all_words = self.get_all_words()  # Получаем все слова
        for file_name, words in all_words.items():
            results[file_name] = words.count(word)  # Сохраняем количество вхождений
        return results


# Пример выполнения программы
if __name__ == "__main__":
    # Создание объекта и выполнение методов
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())  # Все слова
    print(finder.find('TEXT'))  # Позиция первого вхождения
    print(finder.count('teXT'))  # Количество вхождений
