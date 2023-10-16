'''
Задание 16.
Дан текст. Проверить, правильно ли в нем расставлены круглые скобки (т. е.
находится ли справа от каждой открывающей скобки соответствующая ей закрывающая
скобка, а слева от каждой закрывающей — соответствующаяей закрывающая).
'''
text = input()
stack = []
out = 'right'
for char in text:
    if char == "(":
        stack.append(char)
    elif char == ")":
        if len(stack) == 0 or stack[-1] != "(":
            out = 'wrong'
            break
        stack.pop()

if len(stack) > 0:
    print('wrong')
else:
    print(out)
