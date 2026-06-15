import random

words_list = [
    "человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", 
    "история", "женщина", "развитие", "власть", "правительство", "начальник",
    "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин",
    "председатель", "сотрудник", "республика", "личность"
]

# возвращает случайное слово из списка word_list в верхнем регистре
def get_word():
    return random.choice(words_list).upper()

# принимает один аргумент tries – количество попыток угадывания слова
# и возвращает текущее состояние игры в графическом виде
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                r'''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                ''',
                # голова, торс, обе руки, одна нога
                r'''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                r'''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                r'''
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]      

def get_masked_word(word, guessed_letters):
    return ''.join([char if char in guessed_letters else '_' for char in word])

# проверяем что введены русские буквы
def is_valid_upper_text(text):
    return text.isalpha() and all(
        'А' <= char <= 'Я' or char == 'Ё' for char in text
    )

# основная логика игры
def play(word):
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = '_' * len(word)  
    guessed_letters = []               # список угаданных букв
    named_words = []                   # список уже названных букв и слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    print(f'Я загадал слово {word_completion}')
    print(f'У вас {tries} попыток угадать слово')
    print(display_hangman(tries))
    while True:
        w = input('Введите букву или слово: ').upper()
        if not is_valid_upper_text(w):
            print('Надо ввести букву русского алфавита или слово из них!')
            continue
        if len(w) > 1:
            if w == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
            elif w in named_words:
                print('Такой вариант уже был, давайте еще раз')                
                continue
            else:
                print('Загадано другое слово')
                named_words.append(w)
                tries -= 1             
                print(display_hangman(tries))
        else:
            if w in named_words:
                print('Такой вариант уже был, давайте еще раз')                
                continue
            elif w in word:
                guessed_letters.append(w)
                named_words.append(w)
                word_completion = get_masked_word(word, guessed_letters)
                if '_' not in word_completion:
                    print(word_completion)
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    break
            else:
                print('Нет такой буквы')
                named_words.append(w)
                tries -= 1             
                print(display_hangman(tries))

        if tries > 0:
            print(f'Осталось {tries} попыток угадать буквы в слове')
            print(word_completion)
        else:    
            print(f'Вы проиграли!')
            break
    
while True:
    play(get_word())
    if input('Сыграем еще раз? (Да/Нет) : ').lower() == 'да':
        continue
    else:
        break
