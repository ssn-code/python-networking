#!/usr/bin/env python3

import socket
import threading

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()

print("Server started...")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    clients.remove(client)
    client.close()

while True:
    client, addr = server.accept()
    print(f"{addr} Connected")
    clients.append(client)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
