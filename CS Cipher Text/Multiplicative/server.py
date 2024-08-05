import socket

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

  
    decrypted_data = decrypt(encrypted_data, key)

  
    conn.send(decrypted_data.encode())
    conn.close()

if __name__ == "__main__":
    start_server()
