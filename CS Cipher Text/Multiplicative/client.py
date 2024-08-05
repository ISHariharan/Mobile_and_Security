import socket

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

def start_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

   
    text = input("Enter a word: ")
    key = int(input("Enter a key: "))

    if key % 2 == 0:
        print("Warning: Key is even. Encryption may not work as expected.")

   
    encrypted_data = encrypt(text, key)

   
    client_socket.send(encrypted_data.encode())
    client_socket.send(str(key).encode())

    decrypted_data = client_socket.recv(1024).decode()

    print("Decrypted string received from server:", decrypted_data)
    client_socket.close()

if __name__ == "__main__":
    start_client()
