def encrypt_decrypt_string():
    text = input("Enter a word: ")
    key = int(input("Enter a key: "))
    
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                temp = (ord(char) - base + key) % 26 + base
            else:
                base = ord('a')
                temp = (ord(char) - base + key) % 26 + base
            encrypted += chr(temp)
        else:
            encrypted += char

    print("Encrypted string:", encrypted)

 
    decrypted = ""
    for char in encrypted:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                temp = (ord(char) - base - key) % 26 + base
            else:
                base = ord('a')
                temp = (ord(char) - base - key) % 26 + base
            decrypted += chr(temp)
        else:
            decrypted += char

    print("Decrypted string:", decrypted)


encrypt_decrypt_string()
