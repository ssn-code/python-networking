import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter message: ")

    client.sendto(message.encode(), ("localhost", 5000))

    data, addr = client.recvfrom(1024)

    print("Server:", data.decode())

    if message.lower() == "exit":
        break

client.close()
