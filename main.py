from random import randrange


def is_valid(num):
    if num.isdigit():
        return 1 <= int(num) <= 100
    else:
        return False


def is_number_guessing_1_to_100():
    print('Добро пожаловать в числовую угадайку')
    num = randrange(1, 100)
    count = 1

    while True:
        input_num = input('Пожалуйста, введите число от 1 до 100: ')

        if not is_valid(input_num):
            print('А может быть все-таки введете целое число от 1 до 100?')
        elif int(input_num) < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif int(input_num) > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        elif int(input_num) == num:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', count)
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    return continue_game()


def continue_game():
    repeat = input('Хотите сыграть ещё раз? Введите "да" или "нет" ')
    if repeat.lower() == 'да':
        print(is_number_guessing_1_to_100())
    return 'Всего доброго!'


print(is_number_guessing_1_to_100())
