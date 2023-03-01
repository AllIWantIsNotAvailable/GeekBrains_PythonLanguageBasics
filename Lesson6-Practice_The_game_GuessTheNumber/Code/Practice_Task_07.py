import random

# Практическое задание №7:
# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает
# его на листок бумаги. Компьютер начинает его отгадывать предлагая игроку
# варианты чисел. Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать
# “загаданное число больше”. Если компьютер назвал число больше, игрок
# должен выбрать “загаданное число меньше”. Игра продолжается до тех пор
# пока компьютер не отгадает число.

# Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для
# общения с компьютером. Вы можете использовать этот способ или придумать свой.


lower_bound = int(input('Укажите минимальную границу диапазона угадывания числа:\n>>>'))
upper_bound = int(input('Укажите максимальную границу диапазона угадывания числа:\n>>>'))
is_winner = False
guess = upper_bound // 2
count = 0
while not is_winner:
    users_check = input(f'\nРобот: "Я думаю, Вы загадали число {guess}, верно?"\n'
                        '(\n - "=" – угадал!\n'
                        '- ">" - моё число больше!\n'
                        '- "<" - моё число меньше\n)\n>>> ')
    if users_check == '>':
        lower_bound = guess
        guess += (upper_bound - lower_bound) // 2
    elif users_check == '<':
        upper_bound = guess
        guess -= (upper_bound - lower_bound) // 2
    elif users_check == '=':
        is_winner = True
    else:
        continue
    count += 1
else:
    print('Роботы победили роботов!\n'
          f'Секретное число угаданно за {count} попыток! >.<')
