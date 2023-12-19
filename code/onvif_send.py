import socket
import onvif_exaples.py


target_ip = "192.168.47.130"
target_port = 34567

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((target_ip,target_port))

socket.sendall(msg.encode(encoding='utf-8'))

data = socket.recv(100)
msg = data.decode() 
print('echo msg:', msg)

socket.close()
