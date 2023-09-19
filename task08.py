'''
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''
# sentence = 'мама ыл раму'
sentence = input()
sorted_word_list = sorted(sentence.split(), key=len)
print(' '.join(sorted_word_list))
