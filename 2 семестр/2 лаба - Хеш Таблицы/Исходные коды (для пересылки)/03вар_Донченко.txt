# Задание 3:
# Определите, сколько раз встречается каждая из букв в неком тексте.

Text = '''Один, два три 4 три три
4 4 два: 4 успокоение, аллегория
тропики Питон - Питон Питон'''
print(Text, '\n')
D = {}
    
for letter in Text:
    if letter not in D:
        D[letter] = 1
    else:
        D[letter] += 1

Symbols = sorted(D.keys())
for letter in Symbols:
    print('Буква(символ)', letter, 'встречается', D[letter], 'раз')
