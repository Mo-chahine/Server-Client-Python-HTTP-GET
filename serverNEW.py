import socket
import time
import datetime
import uuid


host = ''
port = 8000

now = datetime.datetime.now()

#making the socket
proxy_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
print ("The socket was created!")

#binding the socket to our port
proxy_socket.bind((host, port))
print ("The socket was binded to port", port, "!")

#allowing the socket to listen for incoming connections
proxy_socket.listen(5)
#sockets able to allow 5 connections, anything past 5 will have to wait
print ("The socket is now listening!")


while True:
    #while true, so that its always listening
    #wait for a connection
    client_socket, address = proxy_socket.accept()
    print ("connection was received from: ", address)

    try:
        
        #revcieving at 4096 was the recomended, vs the usual 1024
        ip = client_socket.recv(4096).decode('utf-8')

        request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"

        #creating a socket to connect with our server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        #connecting our socket to the ip
        server_socket.connect((ip, 80))

        #we send the client request to the destination server and show the exact time it was sent
        server_socket. send(request.encode())
        print ("Your request was sent to your server with ip: ", ip, "at: ", now.strftime("%H:%M:%S"), "clocked at time: ", time.time())

        print("ACTUAL request time is: ", time.time())

        #receiving the response from the server
        response = server_socket.recv(4096).decode()
        print ("Your response was received from the server at: ", now.strftime("%H:%M:%S"), "clocked at time: ", time.time())

        #closing the server's socket
        server_socket.close()

        #sending the response back to the client
        client_socket.send(response.encode())
        print ("Your response was returned to the client at:", now.strftime("%H:%M:%S"), "clocked at time: ", time.time())


    #a socket error code i found off of GeeksforGeeks
    except socket.error:
        errormessage = "Server error"
        client_socket.send(errormessage.encode())
        print (b'Error: Server error')


    #closing the client's socket
    finally:
        client_socket.close()
