'''
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
'''
# sentence = 'мама ghbdtn мама привет'
sentence = input()
for word in sentence.split():
    if word in sentence.replace(word, '', 1):
        print(word)
