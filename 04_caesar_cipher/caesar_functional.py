def encrypt_char(char, shift):
    if not char.isalpha():
        return char

    start_code = ord('a') if char.islower() else ord('A')
    return chr(start_code + (ord(char) - start_code + shift) % 26)


def encrypt_word(word):
    shift = sum(1 for char in word if char.isalpha())
    return ''.join(encrypt_char(char, shift) for char in word)


text = input()
new_text = [encrypt_word(word) for word in text.split()]

print(' '.join(new_text))