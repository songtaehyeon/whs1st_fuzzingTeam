import socket
from onvif_examples import process_file,process_db
from db_control import main_db
import random
import os
import string
import time
import requests
import sqlite3
from sqlite3 import Error
from datetime import datetime



target_ip = "192.168.47.130"
target_port = 8899
total_tag = []

random.seed(1234)

cnt = 0

url = f'http://{target_ip}:{target_port}/onvif/device_service'
headers = {
    'Content-Type': 'application/soap+xml; charset=utf-8;',
}

data_folder = "../extract_data/split"
file_list = os.listdir(data_folder)


while 1:
   for file_name in file_list: 
      file_path = os.path.join(data_folder, file_name)
      ori_data = process_file(file_path,total_tag)
      packets = ori_data[0]
      print(packets)
      total_tag = ori_data[1]      
      print('\n\n')
      if cnt >= 3:
         print("ENNDDD")
         break
      else:
         try:
            response = requests.post(url, data=packets, headers=headers)
         except:
            response = ''
      time.sleep(0.1)
      print(cnt)
      cnt += 1
   if cnt >= 3:
      print("ENNDDD")
      break


while 1:
   print("===========IN DB===========")
   new_packets = main_db()
   new_packets = new_packets.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'")
   new_packets = new_packets.splitlines()
   new_packets = process_db(new_packets,total_tag)
   packets = ori_data[0]
   total_tag = ori_data[1]
   try:
      response = requests.post(url, data=packets, headers=headers)
   except:
      response = ''
   time.sleep(0.1)

socket.close()