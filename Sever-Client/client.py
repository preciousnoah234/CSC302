import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
            else:
                break
        except ConnectionResetError:
            break

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode('utf-8'))

    client_socket.close()
    print("Disconnected from server")

if __name__ == "__main__":
    start_client()