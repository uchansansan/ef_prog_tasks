'''
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
'''
# sentence = 'мама ыл раму.'
sentence = input()
print(len(min(sentence.split(), key=len)))
