class WordsFinder:
    def __init__(self, *args):
        self.file_names = args
        self.all_words = self.get_all_words()  # Инициализация all_words

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:  # Используем file_name из self.file_names
            with open(file_name, 'r', encoding='utf-8') as file:
                words_list = []
                for line in file:
                    line = line.lower()
                    line = line.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
                    words = line.split()
                    words_list.extend(words)
                all_words[file_name] = words_list
        return all_words

    def find(self, word):
        word = word.lower()
        for file_name, words in self.all_words.items():
            if word in words:
                return {file_name: words.index(word) + 1}
        return 'Слово не найдено'

    def count(self, word):
        word = word.lower()  # Добавлены скобки
        counts = {}
        for file_name, words in self.all_words.items():
            counts[file_name] = words.count(word)  # Считаем количество
        return counts  # Возвращаем словарь с подсчетами

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))      # 3 слово по счёту
print(finder2.count('teXT'))     # 4 слова teXT в тексте всего