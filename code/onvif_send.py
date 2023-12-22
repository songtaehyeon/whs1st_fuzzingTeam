import socket
from onvif_examples import process_file
import random
import os
import string
import time
import requests

target_ip = "192.168.47.130"
target_port = 8899

random.seed(1234)

cnt = 0

# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.connect((target_ip,target_port))

url = f'http://{target_ip}:{target_port}/onvif/device_service'
headers = {
    'Content-Type': 'application/soap+xml; charset=utf-8;',
}

data_folder = "../extract_data/split"
file_list = os.listdir(data_folder)
while 1:
   for file_name in file_list[0:]: 
      file_path = os.path.join(data_folder, file_name)
      packets = process_file(file_path)
      for pkt in packets:
         print('\n\n'+file_path)
         print(pkt)
         try:
            response = requests.post(url, data=pkt, headers=headers)
         except:
            response = ''
         # socket.sendall(pkt)
         time.sleep(0.1)
         print(cnt)
         cnt += 1


socket.close()