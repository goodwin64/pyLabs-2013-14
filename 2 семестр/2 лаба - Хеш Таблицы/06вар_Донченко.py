# Задание 6:
# Дан текст. Выведите слова, которые встречаются в тексте только по одному разу.

def Only_one_word(Text):
    List_of_words = Text.split() # список слов
    Set_of_words = list(set(List_of_words)) # множество слов
    for E in Set_of_words:
        if List_of_words.count(E) == 1:
            print (E)

Text = input('Text:\n')

print('\n Tekct:\n', Text)

Only_one_word(Text)
