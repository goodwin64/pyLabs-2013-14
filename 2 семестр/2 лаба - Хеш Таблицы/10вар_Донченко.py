# Задание 10:
# Дан текст. Посчитайте, сколько в нем слов, состоящих из 1, 2, …, N букв

def Word_count(Text='', N=10):
    D = {}
    List_of_words = Text.split() # список слов
    for word in List_of_words:
        if len(word) <= N:
            if len(word) not in D:
                D[len(word)] = 1
            else:
                D[len(word)] += 1
    List_of_count_of_words = sorted(D.keys(), reverse = False)
    for x in List_of_count_of_words: # "x" - количество букв, D[x] - количество слов с "х" буквами
        print('Слов, состоящих из {0} букв, в тексте {1}'.format(x, D[x]))

N = int(input('Максимальная длина слова: '))
Text = input('Your text:\n')

Word_count(Text, N)
