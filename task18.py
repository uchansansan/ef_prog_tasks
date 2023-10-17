'''
Задание 18.
Дан текст. По указанному количеству символов в колонке, получите такую колонку
текста с выравниванием по ширине, перенося слова в следующую строку и расставляя
равномерно нужное количество пробелов между словами.
'''
def format_text(text, column_width):
    words = text.split()
    formatted_lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= column_width:
            current_line.append(word)
            current_length += len(word) + 1  # Добавляем длину слова и пробел
        else:
            formatted_lines.append(current_line)
            current_line = [word]
            current_length = len(word) + 1

    if current_line:
        formatted_lines.append(current_line)

    result = ""
    for line in formatted_lines:
        line_length = sum(len(word) for word in line)
        num_words = len(line)
        num_spaces = column_width - line_length

        if num_words == 1 or len(line) == 1:
            result += line[0] + " " * num_spaces
        else:
            spaces_between_words = num_spaces // (num_words - 1)
            extra_spaces = num_spaces % (num_words - 1)

            for i in range(len(line) - 1):
                result += line[i] + " " * spaces_between_words
                if i < extra_spaces:
                    result += " "

            result += line[-1]

        result += "\n"

    return result


text = input("Введите текст: ")
column_width = int(input("Введите ширину колонки: "))

formatted_text = format_text(text, column_width)
print("Результат форматирования:")
print(formatted_text)
