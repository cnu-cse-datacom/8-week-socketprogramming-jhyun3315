from os.path import getsize
import socket

HOST ='168.188.126.209'
PORT = 9090
        
data_transferred = 0
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter file name: ")
socket.sendto(filename.encode(),(HOST,PORT))

filename = filename.encode()
filesize = str(getsize(filename))
socket.sendto(filesize.encode(),(HOST,PORT))
filesize = int(filesize)

print('File Transmit Start...')
f = open(filename, 'rb')
data = f.read(1024)
while data:
    data_transferred += len(data)
    data = f.read(1024)
    socket.sendto(data, (HOST,PORT))
    print('current_size / totalsize = ', data_transferred, '/', filesize,',', (data_transferred / filesize)*100) 
f.close()
print('ok')
print('file_send_end')
socket.close()


