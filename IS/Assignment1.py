# Function to generate repeated key equal to plaintext length
def generate_key(text, key):
    key = key.upper()
    key_extended = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            key_extended += key[key_index % len(key)]
            key_index += 1
        else:
            key_extended += char
    return key_extended
# Function to encrypt plaintext using Vigenère Cipher
def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.upper()
    key_extended = generate_key(plaintext, key)
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key_extended[i]) - ord('A')
            encrypted_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += plaintext[i]
    
    return ciphertext
# Function to decrypt ciphertext using Vigenère Cipher
def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.upper()
    key_extended = generate_key(ciphertext, key)
    plaintext = ""
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key_extended[i]) - ord('A')
            decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += ciphertext[i]
    
    return plaintext
# Main Program
if __name__ == "__main__":
    message = input("Enter the message: ")
    key = input("Enter the key: ")
    
    encrypted = encrypt_vigenere(message, key)
    print("Encrypted Message:", encrypted)
    
    decrypted = decrypt_vigenere(encrypted, key)
    print("Decrypted Message:", decrypted)