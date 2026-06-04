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

while True:
    shift = input('Задайте шаг сдвига (целое число): ')
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

modified_text = []
language_len = len(language_lower) 

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
        
print('Измененный текст:')
print(''.join(modified_text))