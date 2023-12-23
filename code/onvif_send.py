import socket
from onvif_examples import process_file
from fuzzingtable import create_connection
import random
import os
import string
import time
import requests
import sqlite3
from sqlite3 import Error
from datetime import datetime

#SQL 실행
def execute_sql(conn, sql, data=None):
   try:
      c = conn.cursor()
      if data:
         c.execute(sql, data)
      else:
         c.execute(sql)
      conn.commit()
   except Error as e:
      print(e)

#오름순
def select_all_rows(conn):
   skip = 0
   row_num = 0
   sql_select_all = """SELECT COUNT(data) FROM FuzzingTable;"""
   sql_line = """"""
   try:
      c = conn.cursor()
      c.execute(sql_select_all)
      rows = c.fetchall()
      for row in rows:
         row_num = row[0]
   except Error as e:
      print(e)
   for i in range(0,row_num):
      print(i)
      win = random.randrange(0,5)
      if win == 0:
         break
      skip += 1
   sql_line = f"""SELECT * FROM FuzzingTable order by code_coverage desc limit {skip}, 1;""" #이 SQL은 왜 실행이 안되는걸까
   print(sql_line)
   execute_sql(conn,sql_line)

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

#DB연결
conn = create_connection("./test.db")
select_all_rows(conn)

while 1:
   for file_name in file_list[0:]: 
      file_path = os.path.join(data_folder, file_name)
      ori_data = process_file(file_path,total_tag)
      packets = ori_data[0]
      total_tag = ori_data[1]      
      print('\n\n'+file_path)
      try:
         response = requests.post(url, data=packets, headers=headers)

      except:
         response = ''
      # socket.sendall(pkt)
      time.sleep(0.1)
      print(cnt)
      cnt += 1


socket.close()