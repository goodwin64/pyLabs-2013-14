# Задание 5:
# Дан текст. Выведите все слова, встречающиеся в тексте
# по одному на каждую строку. Слова должны быть
# отсортированы по убыванию их количества появления в тексте.

Text = input('Введите текст: ')

List_of_words = Text.split()
Set_of_words = list(set(List_of_words))
D = {}

# Словарь "Частота -> Слово"
for word in Set_of_words:
    if List_of_words.count(word) not in D:
        D[List_of_words.count(word)] = [word]
    else:
        D[List_of_words.count(word)].append(word)

for frequence in sorted(D.keys(), reverse=True):
    for word in sorted(D[frequence]):
        print(word)
