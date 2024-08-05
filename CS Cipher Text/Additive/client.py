import socket

def encrypt_message(text, key):
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
    return encrypted

def start_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    text = input("Enter a word: ")
    key = int(input("Enter a key: "))

    encrypted_data = encrypt_message(text, key)


    client_socket.send(encrypted_data.encode())
    client_socket.send(str(key).encode())


    decrypted_data = client_socket.recv(1024).decode()

    print("Decrypted string received from server:", decrypted_data)
    client_socket.close()

if __name__ == "__main__":
    start_client()
