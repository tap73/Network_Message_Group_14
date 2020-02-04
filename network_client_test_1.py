# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:42:45 2020

@author: tyler
"""
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
    data = input("Data to send to the server: ")

        # When passing data string into the send command received error 
        # that it requires a byte-like object not a string
        
    #send the data
    s.send(data.encode())

    #get response
    reply = s.recv(1024).decode()

    #close connection if told too else continue
        #had to add a b to make sure it read the binary string correctly
        #otherwise it would never recognize the terminate command
    if reply == 'Teminate':
        break
    print(reply)
