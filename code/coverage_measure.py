import socket
from onvif_examples import process_file
from fuzzingtable import *
import random
import os
import string
import time
import requests
import re

##############################################################
target_ip = "192.168.137.136"
target_port = 8899

random.seed(1234)

cnt = 0

url = f'http://{target_ip}:{target_port}/onvif/device_service'
headers = {
    'Content-Type': 'application/soap+xml; charset=utf-8;',
}

data_folder = "../extract_data/split"
file_list = os.listdir(data_folder)
##############################################################

def send_fuzzing_input(file_name):
   file_path = os.path.join(data_folder, file_name)
   packets = process_file(file_path)

   pkt = ''
   response = ' '

   ret_arr = []

   for pkt in packets:
      print('\n\n'+file_path)
      #print(pkt)
      try:
         response = requests.post(url, data=pkt, headers=headers)
      except:
         response = ''
      time.sleep(0.1)

   ret_arr.append(pkt)
   ret_arr.append(response)

   return ret_arr

def get_coverage_count():
   with open('/home/iotfragile/qemu-c300/coverage.txt', 'r') as file:
      lines = file.readlines()
   filtered_lines = [line for line in lines if line.startswith('[2023-')]
   unique_lines = set(filtered_lines)

   result_count = len(unique_lines)
   return result_count

def get_timestamp_from_coverage(cov_count):
   if cov_count == 0:
      return ''

   with open('/home/iotfragile/qemu-c300/coverage.txt', 'r') as file:
      lines = file.readlines()

   # [2023- prefix로 시작하는 라인의 문자열을 배열에 추가
   filtered_lines = [line.strip() for line in lines if line.startswith('[2023-')]

   # 배열의 맨 뒤에 있는 3줄 중에서 첫 번째 줄의 타임스탬프만 가져오기
   if filtered_lines:
      timestamp_line = filtered_lines[-cov_count]
      timestamp_line = re.search(r'\[([^]]*)\]', timestamp_line).group(1)
      # print(timestamp_line)
      return timestamp_line


if __name__ == '__main__':
   conn = create_connection("./test.db")
   drop_table(conn)
   create_table(conn)
   now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

   init_coverage_count = get_coverage_count()

   example_values = [(cnt, 'type' + str(cnt), 'description' + str(cnt), 'count of coverage before running fuzzer, here we go increased coverage count', now, 0, init_coverage_count)]
   for data in example_values:
      insert_example_values(conn, data)
   select_all_rows(conn)

   current_coverage_count = 0

   while True:
      for file_name in file_list[0:]: 
         cnt = cnt+1
         ret_arr = send_fuzzing_input(file_name)
         print(ret_arr)
         print(cnt)
         ret_arr = ', '.join(map(str, ret_arr))
         current_coverage_count = get_coverage_count() - init_coverage_count
         init_coverage_count = get_coverage_count()
         example_values = [(cnt, 'type' + str(cnt), 'description' + str(cnt), ret_arr, get_timestamp_from_coverage(current_coverage_count), 0, current_coverage_count)]
         for data in example_values:
            insert_example_values(conn, data)
         select_all_rows(conn)