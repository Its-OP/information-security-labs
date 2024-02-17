import sys


def generate_key(plaintext: str, key: str) -> str:
    curr_key = key
    while len(plaintext) > len(curr_key):
        curr_key += key

    return curr_key


def encrypt(plaintext: str, key: str):
    cipher_text = []
    base = ord('a')
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) - base + ord(key[i]) - base) % 26
        x += ord('a')
        cipher_text.append(chr(x))
    return ''.join(cipher_text)


def decrypt(ciphertext, key: str):
    orig_text = []
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) - ord(key[i])) % 26
        x += ord('a')
        orig_text.append(chr(x))
    return ''.join(orig_text)


mode = input('Please select the working mode: ')
if mode != 'encrypt' and mode != 'decrypt':
    print(f'Mode {mode} is not supported')
    sys.exit()

key_part = input('Please enter the key: ')
lcs_key_part = key_part.lower()
text_type = 'plaintext' if mode == 'encrypt' else 'ciphertext'
text = input(f'Please enter the {text_type}: ').lower()

full_key = generate_key(text, key_part)
result = encrypt(text, full_key) if mode == 'encrypt' else decrypt(text, full_key)
print(result)
