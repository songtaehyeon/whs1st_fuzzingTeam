import socket
from onvif_examples import process_file
import random
import os
import string
import time

target_ip = "192.168.47.130"
target_port = 8899

random.seed(1234)

cnt = 0

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((target_ip,target_port))

data_folder = "../extract_data/split"
file_list = os.listdir(data_folder)
while 1:
	for file_name in file_list[0:]: 
		file_path = os.path.join(data_folder, file_name)
		print(file_path)
		packets = process_file(file_path)
		for pkt in packets:
			socket.sendall(pkt.encode(encoding='utf-8'))
			time.sleep(0.1)
			print(cnt)
			cnt += 1


socket.close()
