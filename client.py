import socket
import pickle

def receive_resources():
    host = '127.0.0.1'
    port = 54321

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    data = client_socket.recv(1024)
    resources_data = pickle.loads(data)

    client_socket.close()

    return resources_data

if __name__ == "__main__":
    resources = receive_resources()
    print(f"CPU Percent: {resources['cpu_percent']}%")
    print(f"RAM Percent: {resources['ram_percent']}%")
