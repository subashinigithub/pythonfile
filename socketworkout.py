import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12346
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    s1="Thank you for,connecting"
    c.send(s1.encode())
    c.close()
