def encrypt(plain_text, key):
    cipher_text = ""
    for i in plain_text:
        if i.isalpha():
            cipher_text += chr(((ord(i) - ord('a')) * key) % 26 + ord('a'))
        else:
            cipher_text += i
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    inverse = pow(key, -1, 26)
    for i in cipher_text:
        if i.isalpha():
            plain_text += chr(((ord(i) - ord('a')) * inverse) % 26 + ord('a'))
        else:
            plain_text += i
    return plain_text 


str = input("Enter a word : ")
key = int(input("Enter a key : "))


cipher_text = encrypt(str, key)
print("Encrypted Code : ", cipher_text)

plain_text = decrypt(cipher_text, key)
print("Decrypted Code : ", plain_text)