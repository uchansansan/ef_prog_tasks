'''
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова,
в слове нет повторяющихся букв.
'''
sentence = input()

words = sentence.split()
res = []

for i in range(1, len(words)):
    if len(set(words[i])) == len(words[i]):
        res.append(words[i])

print(' '.join(res))
