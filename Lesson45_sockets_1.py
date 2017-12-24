import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # opening TCP socket
server = 'pythonprogramming.net'
port = 80 #http
serverIp = socket.gethostbyname(server) # getting the host ip adress
# making a get request
request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pythonprogramming.net", 80)) # or (server, port)
s.send(request.encode()) # python 3 needs to encode before sending
result = s.recv(4096) # 4096 is the buffer
# reading needs loop because of the buffer
while (len(result) > 0):
    print(result)
    result = s.recv(4096)

