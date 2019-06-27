# client2.py
#!/usr/bin/env python
from test import server_config
import socket

TCP_IP = server_config(1)
TCP_PORT = server_config(5)
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
with open('received_file', 'wb') as f:
    print ('file opened')
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print('data=%s', (data))
        if not data:
            f.close()
            print ('file close()')
            break
        # write data to a file
        f.write(data)

print('Successfully get the file')
s.close()
print('connection closed')
