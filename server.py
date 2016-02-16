# UDPPingServer.py
# We will need the random module to generate randomized lost packets
import random,time
from socket import *
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM) # Assign IP address and port number to socket
serverSocket.bind(('', 12000))
#The loop runs for ever
while True:
 # Generate random number in the range of 0 to 10
 rand = random.randint(0, 10)
 # Receive the client packet along with the address it is coming from
 message, address = serverSocket.recvfrom(1024)
 # simulate a delay between .1 to .5 seconds
 rand2 = random.randint(1,5)/10.0
 time.sleep(rand2)
 # If rand is less is than 4, we consider the packet lost and do not respond
 if rand < 4:
    continue
 # Otherwise, the server responds
 serverSocket.sendto(message, address)
 
