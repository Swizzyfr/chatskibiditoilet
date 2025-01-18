import socket

# Replace with the correct server IP address
SERVER_IP = "192.168.88.238"  # Use the server's local IP address
PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server using the local IP address
client_socket.connect((SERVER_IP, PORT))

# Get the username of the device running the client
username = input("Enter your username: ")

# Send the username to the server
client_socket.send(username.encode('utf-8'))

# Receive and send messages
while True:
    message = input(f"{username}: ")
    if message.lower() == 'exit':
        break
    client_socket.send(message.encode('utf-8'))

client_socket.close()
