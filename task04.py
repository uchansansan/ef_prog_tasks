'''
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
'''
# text = 'uvvvu'
text = input()
chars = {}
for char in text:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1
    if chars[char] == 3:
        print(char)
        break
