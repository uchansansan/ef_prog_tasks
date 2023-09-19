'''
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова,
в слове нет повторяющихся букв.
'''
# sentence = 'марш привет марш*'
sentence = input()

new_sentence = ''
for char in sentence:
    if not char.isalpha():
        new_sentence = sentence.replace(char, '')

words = new_sentence.split()

for word in words:
    if word != words[0] and len(word) == len(set(word)):
        print(word)
