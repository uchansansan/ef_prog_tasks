'''
Задание 14.
В телевизионной игре "Поле чудес", игрок отгадывает слово. Напишите программу, которая спрашивает
у ведущего подсказку и загаданное слово. Далее, программа удаляет информацию с экрана, выполняя
вывод 25 пустых строк. После этого, выводится подсказка и слово, где вместо букв, выводятся
символы "*". Игрок должен с десяти попыток отгадать слово по буквам. После каждого хода выводится
слово, где неназванные буквы закрыты символом "*".  Отгаданные буквы выводятся на тех местах, где
они расположены. Каждый ход сопровождается вопросом "Буква или слово (0 - буква, 1 - слово)?".
В случае если слово отгадано верно, выводится сообщение "Победа!". Если слово названо неверно,
или закончились попытки, выводится сообщение "Проигрыш!".

Пример работы программы:
Ведущий вводит две строки: подсказку и загаданное слово.
Дикое животное.
тигр
Программа выводит 25 пустых строк и таким образом "скрывает" то, что написал ведущий.
Игрок пытается отгадать слово:
Дикое животное.
****
Буква или слово (0 - буква, 1 - слово)?0
a
****
Буква или слово (0 - буква, 1 - слово)?0
р
***р
Буква или слово (0 - буква, 1 - слово)?0
и
*и*р
Буква или слово (0 - буква, 1 - слово)?1
тигр
Победа!
'''
hint = input('Подсказка: ')
word = input('Слово: ')

print('\n' * 25)

print(f'Подсказка: {hint}')
current_word = ['*'] * len(word)


def letter_indices(letter, word):
    indices = []
    inx = 0
    while word.find(letter, inx) != -1:
        inx = word.find(letter, inx)
        print(inx)
        indices.append(inx)
        inx += 1
    return indices


for step in range(10):
    print(f'Осталось попыток: {10 - step}')
    mode = int(input('Буква или слово (0 - буква, 1 - слово)? '))
    if mode == 0:
        letter = input()
        indicies = letter_indices(letter, word)
        for i in indicies:
            current_word[i] = word[i]
        print(''.join(current_word))
        if ''.join(current_word) == word:
            print('Победа!')
            break
    elif mode == 1:
        attempt = input()
        if attempt == word:
            print('Победа!')
        else:
            print('Проигрыш!')
        break
else:
    print('Проигрыш!')
