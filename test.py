import hashlib
import socket


def server_config(a=0):
    ip1 = socket.gethostbyname(socket.gethostname())
    ip2 = ip1
    host = str(ip2)    # Server configurations
    chat_port = 3000
    video_port = 4000
    audio_port = 5000
    TCP_Port = 9001
    if a == 1:
        return host
    elif a == 2:
        return video_port
    elif a == 3:
        return audio_port
    elif a == 4:
        return chat_port
    elif a == 5:
        return TCP_Port
    elif a == 6:
        return ip1


def split(a, b=1):
    sep = ' '
    if b == 1:                        # code to split username
     uname = a.split(sep, 1)[0]
     return uname.lower()
    elif b == 2:
        addr1 = format(a)               # code to split ip address
        addr2 = addr1.split(sep, 1)[0]
        addr2 = addr2.replace('(', '')
        addr2 = addr2.replace(',', '')
        return addr2


def encrypt_code(p):
    m = hashlib.md5()
    m.update(p.encode('utf-8'))
    p2 = m.hexdigest()
    return p2
