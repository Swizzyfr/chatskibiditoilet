import socket
import threading
import sys

# This will allow the client to connect to a specific IP address and port
server_ip = '127.0.0.1'  # Change this if you're using a different IP
server_port = 5555

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')  # Receiving data from the server
            if message:
                print(message)  # Print message from server
            else:
                break
        except:
            print("Error receiving message.")
            break

# Function to send messages to the server
def send_messages():
    while True:
        message = input("You: ")  # Input from the user
        if message.lower() == 'exit':
            client_socket.send("User has left the chat.".encode('utf-8'))
            break
        client_socket.send(f"User: {message}".encode('utf-8'))  # Send message to server

# Start threads for receiving and sending messages
thread_receive = threading.Thread(target=receive_messages)
thread_receive.start()

thread_send = threading.Thread(target=send_messages)
thread_send.start()
