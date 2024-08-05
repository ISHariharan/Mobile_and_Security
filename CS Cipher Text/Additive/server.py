import socket

def decrypt_message(encrypted, key):
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
    return decrypted

def start_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening on port", port)

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")


    encrypted_data = conn.recv(1024).decode()
    key = int(conn.recv(1024).decode())


    decrypted_data = decrypt_message(encrypted_data, key)


    conn.send(decrypted_data.encode())
    conn.close()

if __name__ == "__main__":
    start_server()
