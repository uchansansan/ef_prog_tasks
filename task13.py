'''
Задание 13.
Дима часто пользуется общественным транспортом и всегда проверяет номер билета,
является ли он "счастливым". Счастливым считается билет, имеющий в номере четное
количество цифр. Причем,  сумма цифр первой половины номера равна сумме цифр
второй половины.  Программа на вход получает  последовательность номеров билетов.
Ввод номеров должен завершить тогда, когда будет введен "счастливый" билет.
Программа должна вывести его порядковый номер. Счет начинается с 1.
'''
cnt = 0
lucky = False

def lucky_check(ticket):
    lenth = len(ticket)
    if lenth % 2 == 0:
        part1 = ticket[:lenth // 2]
        part2 = ticket[lenth // 2:]
        part1_sum, part2_sum = 0, 0

        for i in range(lenth // 2):
            part1_sum += int(part1[i])
            part2_sum += int(part2[i])

        return part1_sum == part2_sum
    else:
        return False


while not lucky:
    ticket = input()
    lucky = lucky_check(ticket)
    cnt += 1
else:
    print(cnt)
