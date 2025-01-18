import socket
import threading
import os

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error receiving message.")
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    # Get the device's username from the OS
    device_username = os.getlogin()

    print("Connected to server. Start chatting!")
    
    # Start listening for incoming messages in a separate thread
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    
    # Start sending messages with device username
    send_messages(client_socket)

start_client()
