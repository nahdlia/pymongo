import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
j = '{"nama" : "sances", "umur" : "30", "Alamat" : "nggak dibawa sayang"}'

def ts(str):
    s.send(j.encode())
    data = ''
    data = s.recv(1024).decode()
    print (data)

while 2:
   r = input('enter')
   ts(s)

s.close ()
