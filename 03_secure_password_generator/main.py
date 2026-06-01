import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

# Переменная chars будет содержать в себе все разрешенные символы,
# которые пользователь выберет для генерации (цифры, буквы, знаки).
# Позже мы будем вытаскивать из нее случайные элементы.

# Программа должна запрашивать у пользователя следующую информацию:
#    Количество паролей для генерации;
#    Длину одного пароля;
#    Включать ли цифры 0123456789?
#    Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
#    Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
#    Включать ли символы !#$%&*+-=?@^_?
#    Исключать ли неоднозначные символы il1Lo0O?

# основании введенной пользователем информации, сформируйте переменную 
# chars, содержащую все символы, которые могут быть в генерируемом пароле.

# Напишите функцию generate_password(), которая принимает два аргумента:
#    length: длину пароля;
#    chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
# Используя цикл for, сгенерируйте необходимое количество паролей.

chars = '' 

print('*** Добро пожаловать в программу генерации паролей ***')
text_p = input('Сколько паролей создать?: ')

# проверка, количество паролей должно быть числом
while not text_p.isdecimal():
    text_p = input('Введите целое число: ')
p = int(text_p)

text_l = input('Какой длины делаем пароль ?: ')

# проверка, длина пароля должно быть числом
while not text_l.isdecimal():
    text_l = input('Введите целое число: ')
l = int(text_l)

if input('Включать ли цифры 0123456789? Да/Нет: ').lower() == 'да':
    chars += digits

if input(
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Да/Нет: '
).lower() == 'да':
    chars += uppercase_letters

if input(
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Да/Нет: '
).lower() == 'да':
    chars += lowercase_letters

if input(
    'Включать ли символы !#$%&*+-=?@^_? Да/Нет: '
).lower() == 'да':
    chars += punctuation

if input(
    'Исключать ли неоднозначные символы il1Lo0O? Да/Нет: '
).lower() == 'да':
    chars = ''.join([c for c in chars if c not in 'il1Lo0O'])

for i in range(p):
    print(f'Пароль_{i}: {generate_password(l, chars)}')
    
