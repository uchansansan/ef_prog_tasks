'''
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
'''
# text = 'мама ммммыла рамууууу'
text = input()
num = 1
max_global = 0
for i in range(0, len(text) - 1):
    if text[i] == text[i + 1]:
        num += 1
    else:
        max_global = max(max_global, num)
        num = 1
print(max_global)
