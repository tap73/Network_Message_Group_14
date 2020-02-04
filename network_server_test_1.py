# -*- coding: utf-8 -*-
"""
TCP_Server_test
Created on Thu Jan 23 15:37:22 2020

@author: tyler
"""

import socket
import time


## Define Function for logging
def log_rx_data (data, log_file):
    #open log file
    f = open(log_file, 'a')
    #write data
    f.write(str(data)+"\n")
    #close File
    f.close()

## Define Varaibles
LOG_FILE = "test_log.txt"
HOST = 'localhost' #server IP address
PORT = 8135 #Pick open port to open socket on

#create socket (socket.socket inputs are (familt, type, protocol))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print("The Socket has been created on the server side")
    # AF_INET defines IPv4 family and expects bind to happen on tuple (HOST,PORT)
    # SOCK_STREAM defines socket type as TCP, SOCK_DGRAM defines UDP

#After socket creation you must bind to associate socket with server addr
#when doing this it is beneficial to manage errors using try/except methods
try: 
    s.bind((HOST,PORT))
except:
    print("Socket Bind to Server Failed")
    
#allow socket to accept new connections i.e. listen... input is number of backloged unnaccepted connections (they queue, convention dictates 5 as system max)
s.listen(5)
print('Socket is listening')
    
#set an open connection to client and server using socket.accept
connection, client_addr = s.accept()
print('Connected to client')

#infinite while to wait for messages
while True: 
    
    #default reply
    reply = "This is a test"
    
    #receive data from connection input is buffersize, or maximum amount acccepted at a time
    rx_data = connection.recv(1024).decode()
    print('I got some data, writing data to log file')
    
    log_rx_data(rx_data, LOG_FILE)
    
    if rx_data == 'quit':
        connection.send('Terminating'.encode())
        break
    
    connection.send(reply.encode())
connection.close() #Close Connecions
