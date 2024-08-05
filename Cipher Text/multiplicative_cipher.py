def encrypt(plain_text, key):
    cipher_text = ""
    for i in plain_text:
        if i.isalpha():
            if i.islower():
                base = ord('a')
            else:
                base = ord('A')
            cipher_text += chr(((ord(i) - base) * key) % 26 + base)
        else:
            cipher_text += i
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    inverse = pow(key, -1, 26)
    for i in cipher_text:
        if i.isalpha():
            if i.islower():
                base = ord('a')
            else:
                base = ord('A')
            plain_text += chr(((ord(i) - base) * inverse) % 26 + base)
        else:
            plain_text += i
    return plain_text 


str_input = input("Enter a word: ")
key = int(input("Enter a key: "))

if key % 2 == 0:
    print("It will not work as the key is even")


cipher_text = encrypt(str_input, key)
print("Encrypted Code: ", cipher_text)

plain_text = decrypt(cipher_text, key)
print("Decrypted Code: ", plain_text)
