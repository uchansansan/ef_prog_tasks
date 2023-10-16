'''
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''
# sentence = 'мама ыл раму'
sentence = input()
sentence_new = (sentence.replace('.', '')
            .replace('!', '')
            .replace('?', '')
            .replace(',', '')
            .replace(':', '')
            .replace(';', ''))
sorted_word_list = sorted(sentence_new.split(), key=len)
print(' '.join(sorted_word_list))
