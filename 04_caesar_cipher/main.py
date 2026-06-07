# Описание проекта: требуется написать программу, способную шифровать 
# и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна 
# запрашивать у пользователя следующие данные:

#    направление: шифрование или дешифрование;
#    язык алфавита: русский или английский;
#    шаг сдвига (со сдвигом вправо).

# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — 
# не меняются.

# Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не 
# понять" при сдвиге на одну позицию вправо 
# будет преобразован в: "Фнпн Спттйя ож рпоауэ".

# Составляющие проекта:

#    Целые числа (тип int);
#    Модульная арифметика;
#    Переменные;
#    Ввод / вывод данных (функции input() и print());
#    Условный оператор (if/elif/else);
#    Цикл for/while;
#    Строковые методы.

def caesar_cipher(
        original_text, shift, direction, language_lower, language_upper
):

    modified_text = []

    for c in original_text:
        if c in language_lower:
            modified_text.append(language_lower[
                (language_lower.index(c) + shift * direction) % language_len
            ])
        elif c in language_upper:
            modified_text.append(language_upper[
                (language_upper.index(c) + shift * direction) % language_len
            ])
        else:
            # Неалфавитные символы (пробелы, знаки) просто переносим как есть
            modified_text.append(c)

    return ''.join(modified_text)

print('*** Шифровщик Цезаря ***')

while True:
    text = input(
        'Выберите направление шифрование или дешифрование (ш/д): '
    ).lower()
    if text == 'ш':
        direction = 1 # right
        break
    elif text == 'д':
        direction = -1 # left
        break
    else:
        print('Выберите из предложенного "ш" или "д"')
        continue

while True:
    text = input(
        'Выберите язык алфавита: русский или английский (р/а): '
    ).lower()
    if text == 'р':
        language_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        language_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        break
    elif text == 'а':
        language_lower = 'abcdefghijklmnopqrstuvwxyz'
        language_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        break
    else:
        print('Выберите из предложенного (русские буквы) "р" или "а"')
        continue

language_len = len(language_lower) 

while True:
    shift = input(
        'Задайте шаг сдвига (целое число),\n'
        'если задать 0, то будет выполнен перебор всех возможных сдвигов,\n'
        'если задать 100, то будет выполно шифрование каждого слова \n'
        'по отдельности со сдвигом равным его длине: '
    )
    if not shift.isdecimal():
        print('Введите целое число!')
        continue
    else:
        shift = int(shift)
        break

while True:
    original_text = input('Введите текст: ')
    if original_text:
        break

if shift == 0:
    print(f'Измененный текст (перебор всех вариантов):')
    for i in range(language_len):
        print(f'cдвиг {i * direction}: ', end='')
        print(caesar_cipher(
            original_text, i, direction, language_lower, language_upper
        ))
elif shift == 100:
    print(f'Измененный текст (сдвиг на длину слова):')
    modified_words = []
    for word in original_text.split():
        len_word = sum(1 for char in word if char.lower() in language_lower)
        
        # В этой задаче на Степике всегда идет шифрование (direction=1)
        modified_words += [
            caesar_cipher(word, len_word, 1, language_lower, 
                          language_upper)
        ]
    print(' '.join(modified_words))
else:
    print(f'Измененный текст со сдвигом {shift * direction}:')
    print(caesar_cipher(
        original_text, shift, direction, language_lower, language_upper
    ))
