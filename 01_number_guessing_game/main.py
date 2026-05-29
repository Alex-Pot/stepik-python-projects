from random import randint

def is_valid_n(text_n):
    return text_n.isdigit() and 1 < int(text_n)

def is_valid_num(text, n):
    return text.isdigit() and 1 <= int(text) <= n


def play(n):
    print(f'\nЗагадал число от 1 до {n} включительно!')
    print(f'Введите число от 1 до {n}:', end='')
    cnt = 0
    secret_num = randint(1, n)

    while True:
        text = input()
        if not is_valid_num(text, n):
            print(f'А может быть все-таки введем целое число от 1 до {n}?:', end='') 
            continue
        else:
            num = int(text)
            cnt += 1
            if num == secret_num:
                print(f'Угадали! за {cnt} попыток')
                break
            elif num < secret_num:
                print('Меньше загаданного, давайте новый вариант:', end='')
            else:
                print('Больше загаданного, давайте новый вариант:', end='')

print('Числовая угадайка!')
while True:
    print('\nЯ загадаю число в интервале от 1 до n, а вы отгадайте')
    print('Введите число n больше 1:', end='')
    while True:
        text_n = input()
        if not is_valid_n(text_n):
            print('Может быть все-таки введем целое число больше 1:', end='') 
            continue
        else:
            n = int(text_n)
            break
    play(n)    
    if input('\nСыграем еще раз? Да/Нет:') != 'Да':
        print('Спасибо за игру! До встречи.')
        break

