import socket



host = 'data.pr4e.org'
port = 80

# Define the path to the file
path = '/intro-short.txt'

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send an HTTP GET request
request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
client_socket.sendall(request.encode())

response = b''
while True:
    part = client_socket.recv(1024)
    if part:
        response += part
    else:
        break

# Close the socket
client_socket.close()

# Decode and print the response
print(response.decode())
