from math import ceil


def _column_order(key):
    indexed_key = list(enumerate(key))
    indexed_key.sort(key=lambda item: (item[1], item[0]))
    return [index for index, _ in indexed_key]


def encrypt_columnar_transposition(plaintext, key, padding_char="X"):
    if not key:
        raise ValueError("Key cannot be empty.")

    columns = len(key)
    rows = ceil(len(plaintext) / columns) if plaintext else 1
    padded_length = rows * columns
    padded_text = plaintext.ljust(padded_length, padding_char)

    matrix = []
    for row in range(rows):
        start = row * columns
        matrix.append(list(padded_text[start:start + columns]))

    order = _column_order(key)
    ciphertext = ""
    for col in order:
        for row in range(rows):
            ciphertext += matrix[row][col]
    return ciphertext


def decrypt_columnar_transposition(ciphertext, key, padding_char="X"):
    if not key:
        raise ValueError("Key cannot be empty.")

    columns = len(key)
    rows = ceil(len(ciphertext) / columns) if ciphertext else 1
    padded_length = rows * columns
    padded_text = ciphertext.ljust(padded_length, padding_char)

    matrix = [[""] * columns for _ in range(rows)]
    order = _column_order(key)

    index = 0
    for col in order:
        for row in range(rows):
            matrix[row][col] = padded_text[index]
            index += 1

    plaintext = ""
    for row in matrix:
        plaintext += "".join(row)
    return plaintext.rstrip(padding_char)


if __name__ == "__main__":
    mode = input("Enter mode (E for Encrypt, D for Decrypt): ").strip().upper()
    text = input("Enter text: ")
    key = input("Enter key: ")

    if mode == "E":
        print("Ciphertext:", encrypt_columnar_transposition(text, key))
    elif mode == "D":
        print("Plaintext:", decrypt_columnar_transposition(text, key))
    else:
        print("Invalid mode. Use E or D.")
