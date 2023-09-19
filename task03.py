'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''
text = input()
letters = {}

for i in text:
    if i not in letters.keys() and i.isalpha():
        letters[i] = 1
    elif i.isalpha():
        letters[i] += 1
print(letters[max(letters)])
