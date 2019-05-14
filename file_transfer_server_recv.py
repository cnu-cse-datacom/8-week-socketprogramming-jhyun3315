import socket

HOST = ''
PORT = 9090

data_transferred =0
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('',PORT))

filename, addr = socket.recvfrom(1024)
filesize, addr = socket.recvfrom(1024)

print("file recv start from", addr[0])
print('File Name: ',filename.decode())
print('File Size: ',filesize.decode())

with  open(filename.decode(), 'wb') as f:
    data, addr = socket.recvfrom(1024)
    while data:
        f.write(data)
        data_transferred += len(data)
        data = socket.recvfrom(1024)
        print('current_size / totla_size= ', data_transferred, '/', filesize.decode(), ',',(data_transferred/filesize.decode())*100)

f.close()
socket.close()
                    
