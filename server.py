import socket
import pickle
import psutil

def get_system_resources():
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    return {'cpu_percent': cpu_percent, 'ram_percent': ram_percent}

def start_server():
    host = '127.0.0.1'
    port = 54321

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        resources_data = get_system_resources()
        serialized_data = pickle.dumps(resources_data)

        client_socket.send(serialized_data)

        client_socket.close()

if __name__ == "__main__":
    start_server()
