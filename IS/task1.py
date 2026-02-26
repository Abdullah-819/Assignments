# I am making a simple encrypter using the Python programming language.

KEY = "Abdullah Rana"
SHIFT = 11
ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = ALPHABET_LOWER.upper()


def _clean_key(key):
    letters = [ch.lower() for ch in key if ch.isalpha()]
    if not letters:
        raise ValueError("Key must contain at least one alphabetic character.")
    return letters


def _normalize_shift(shift):
    while shift < 0:
        shift += 26
    while shift >= 26:
        shift -= 26
    return shift


def _rotate_char(ch, shift):
    shift = _normalize_shift(shift)
    if ch in ALPHABET_LOWER:
        rotated = ALPHABET_LOWER[shift:] + ALPHABET_LOWER[:shift]
        return rotated[ALPHABET_LOWER.index(ch)]
    if ch in ALPHABET_UPPER:
        rotated = ALPHABET_UPPER[shift:] + ALPHABET_UPPER[:shift]
        return rotated[ALPHABET_UPPER.index(ch)]
    return ch


def _unrotate_char(ch, shift):
    shift = _normalize_shift(shift)
    if ch in ALPHABET_LOWER:
        rotated = ALPHABET_LOWER[shift:] + ALPHABET_LOWER[:shift]
        return ALPHABET_LOWER[rotated.index(ch)]
    if ch in ALPHABET_UPPER:
        rotated = ALPHABET_UPPER[shift:] + ALPHABET_UPPER[:shift]
        return ALPHABET_UPPER[rotated.index(ch)]
    return ch


def enc_substitution(plaintext):
    result = ""
    key_letters = _clean_key(KEY)
    key_index = 0

    for ch in plaintext:
        if ch.isalpha():
            key_shift = ALPHABET_LOWER.index(key_letters[key_index])
            total_shift = _normalize_shift(key_shift + SHIFT)
            result += _rotate_char(ch, total_shift)
            key_index += 1
            if key_index == len(key_letters):
                key_index = 0
        else:
            result += ch
    return result


def dec_substitution(ciphertext):
    result = ""
    key_letters = _clean_key(KEY)
    key_index = 0

    for ch in ciphertext:
        if ch.isalpha():
            key_shift = ALPHABET_LOWER.index(key_letters[key_index])
            total_shift = _normalize_shift(key_shift + SHIFT)
            result += _unrotate_char(ch, total_shift)
            key_index += 1
            if key_index == len(key_letters):
                key_index = 0
        else:
            result += ch
    return result


origitext = input("Enter the text you want to encrypt: ")
ciphertext = enc_substitution(origitext)
plaintext = dec_substitution(ciphertext)
print("Key used:", KEY)
print("Shift used:", SHIFT)
print("Ciphertext:", ciphertext)
print("Decrypted text:", plaintext)
print(origitext)
