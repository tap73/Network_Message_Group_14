## Senior Design Group 14
## Network Message Client Test Application
## Tyler Pizzo (tap73@drexel.edu)

import socket

## Define Varaibles
LOG_FILE = "test_log.txt"
HOST = 'localhost' #server IP address
PORT = 8135 #Pick open port to open socket on

## Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client Socket Created")

## connect to the server
s.connect((HOST,PORT))
print("Connected to Server")

while True:
    
    #ask for data
    data_select = input("1, 2, or 3? \n")

    if data_select == '1':
        data = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'
    if data_select == '2':
        data = '17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33'
    if data_select == '3':
        data = 'quit'

        # When passing data string into the send command received error 
        # that it requires a byte-like object not a string
        
    #send the data
    s.send(data.encode())

    #get response
    reply = s.recv(1024).decode()

    #close connection if told too else continue
        #had to add a b to make sure it read the binary string correctly
        #otherwise it would never recognize the terminate command
    if reply == 'Terminating':
        break
    print(reply)
