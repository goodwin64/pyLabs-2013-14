# Задание 8:
# Дан текст. Выведите слова, которые встречаются в тексте по несколько раз.

def Not_unique_words(Text):
    List_of_words = Text.split() # список слов
    Set_of_words = list(set(List_of_words)) # множество слов
    for E in Set_of_words:
        if List_of_words.count(E) != 1:
            print(E)      

Text = input('Your text:\n')

Not_unique_words(Text)
