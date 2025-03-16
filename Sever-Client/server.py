import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {client_address}: {message}")
                response = f"Server received: {message}"
                client_socket.sendall(response.encode('utf-8'))
            else:
                break
        except ConnectionResetError:
            break
    print(f"Connection closed with {client_address}")
    client_socket.close()

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()