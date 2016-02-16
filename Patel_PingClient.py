import socket 
import time
import sys
from socket import *
RTT = []
serverName = sys.argv[1]
clientSocket = socket(AF_INET,SOCK_DGRAM) 
clientSocket.settimeout(1)
sequence_number = int(sys.argv[3])
count = 1
while count<=sequence_number:
	message = 'Ping'
	start=time.time() 
	localtime = time.asctime( time.localtime(time.time()) )
	clientSocket.sendto(message,(serverName, int(sys.argv[2])))
	try:
		modifiedmessage, address = clientSocket.recvfrom(2048)
		elapsed = (time.time()-start)
		RTT.append(elapsed)
		print "Reply from " + str(serverName) + " : " + str(modifiedmessage) + " " + str(count) + " " + str(localtime)
		print 'RTT: ' + str(elapsed)
	except timeout:
		print 'Requested timed out'
	count = count + 1 
	if count > sequence_number:
		clientSocket.close()
print  "Max = " + str(max(RTT)) + " " + "Min = " + str(min(RTT)) + " " + "Average = " + str((reduce(lambda x, y: x + y, RTT) / len(RTT))) + " " + "Packet loss = " + str((((sequence_number - len(RTT))*100)/sequence_number)) + "%"
