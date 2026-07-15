#!/usr/bin/env python3

import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\nFriend:", message)
        except:
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    message = input()

    if message.lower() == "exit":
        break

    client.send(message.encode())

client.close()
