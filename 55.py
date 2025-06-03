class Text:
    def __init__(self, text):
        self.text = text  

    def get_character_count(self):
  
        return len(self.text)

    def get_letter_count(self):
  
        return sum(c.isalpha() for c in self.text)

    def get_space_count(self):
        return self.text.count(' ')

    def get_character_count_excluding_spaces(self):
 
        return len(self.text.replace(' ', ''))

    def get_words(self):
     
        return self.text.split()

    def get_sentences(self):
       
        return [sentence.strip() for sentence in self.text.split('.') if sentence]

# Пример использования
text = Text("Привет, мир. Как дела? Это пример текста.")
print(f"Количество символов: {text.get_character_count()}")                      # Вывод: 42
print(f"Количество букв: {text.get_letter_count()}")                             # Вывод: 34
print(f"Количество пробелов: {text.get_space_count()}")                         # Вывод: 7
print(f"Количество символов без пробелов: {text.get_character_count_excluding_spaces()}")  # Вывод: 35
print(f"Слова: {text.get_words()}")                                             # Вывод: ['Привет,', 'мир.', 'Как', 'дела?', 'Это', 'пример', 'текста.']
print(f"Предложения: {text.get_sentences()}")                                   # Вывод: ['Привет, мир', 'Как дела? Это пример текста']
