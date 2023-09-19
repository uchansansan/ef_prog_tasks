'''
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
'''
text = input()
num = 1
max_global = 0
for i in range(0, len(text) - 1):
    if text[i] == text[i + 1] and text[i] == ' ':
        num += 1
        max_global = max(max_global, num)
    else:
        num = 1
print(max_global)
