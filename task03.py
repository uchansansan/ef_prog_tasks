'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''
text = input()
letters = []

for char in text:
    if char not in letters and char.isalpha():
        letters.append(char)

print(len(letters))
