import socket
from config import TIMEOUT

def scan_port(host,port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result=sock.connect_ex((host,port))
        sock.close()
        return result==0
    except:
        return False
