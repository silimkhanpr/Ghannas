import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Connect to an IP with Port, could be a URL
sock.connect(('172.26.10.200', 8080))

## Send some data, this method can be called multiple times
str="hello"
sock.send(str.encode("utf8"))

c=input("Do you want to send a file")
if c=='y':
    filename='m.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        sock.send(l)#.encode("utf8"))
        print('Sent ',repr(l))
        l = f.read(1024)
        f.close()

else:
    ## Receive up to 4096 bytes from a peer
    msg=sock.recv(4096)
    print(msg)

## Close the socket connection, no more data transmission
sock.close()
