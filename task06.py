'''
Задание 6.
Дано предложение. Напечатать его в обратном порядке слов.
'''
#sen = 'Мама мыла раму, и пила кофе?'
sen = input()
print(' '.join(sen.split()[::-1]))