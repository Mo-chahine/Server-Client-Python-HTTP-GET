import socket
import time
import datetime
import uuid


host = '127.0.0.1'
port = 8000

now = datetime.datetime.now()

#making the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#asking the user to imput the ip address of a website of their choice
ip = input('ENTER an IP address: ')

#connecting the client socket to a local host and the port number of the server
#a classmate helped me with this code
client_socket.connect(('localhost', port))



#recording the time
start_time = time.time()


#sending our IP address to the server as per request
client_socket.send(ip.encode())
print ("Your request was sent to the Server at: ", now.strftime("%H:%M:%S"), "clocked at time: ", time.time())

#we're recieiving the servers response to our earlier request, at 4096
response = client_socket.recv(4096).decode()
print ("the server responsed with: ", response, "\n", "You recieved the response at: ", now.strftime("%H:%M:%S"), "clocked at time", time.time())

#for RoundTripTime calculation
end_time = time.time()
RTT = end_time - start_time


#code found on CodeSpeedy.com, MAC Addresses on Python
MACaddress = ':'.join(format(s, '02x') for s in uuid.getnode().to_bytes(6, 'big'))

print ("IP: ", ip)
print ("MAC address: ", MACaddress)
print ("Round Trip Time:", RTT)


client_socket.close()
