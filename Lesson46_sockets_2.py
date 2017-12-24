import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('What website to scan?: ')

# defining a port scanner
def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(1024):
    if pscan(x):
        print('Port',x,'is open')	
    else:
        print('port', x, 'is closed!')