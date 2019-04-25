#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = open('hashes.txt','r').readlines()
    passwords = open('passwords.txt','r').readlines()
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    for x in range(3):
        data = s.recv(1024)
        data = data.splitlines()
        data = data[2]
        print(data)
        for c in characters:
            for p in passwords:
                c = c.strip()
                p = p.strip()
                input = c+p
                hash = hashlib.sha256(input.encode())
                if hash.hexdigest().strip() == data.strip():
                    print(input)
                    time.sleep(5)
                    s.send(input+"\n")
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()
