import os
import random
import string

def data_change(input_line):
    output_line = ""
    i = 0
    while i < len(input_line):
        if input_line[i] == "?":
            random_str = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(5, 50)))
            output_line += random_str
            i += 1
        else:
            output_line += input_line[i]
            i += 1
    return output_line

def process_file(file_path):
    with open(file_path, 'r') as file:
        file_data = file.readlines() #파일안의 내용이 리스트로 나옴
        for file_line in range(len(file_data)): # 라인 별로 체크
            line = file_data[file_line] #file_line 번째 줄이 나옴
            file_data[file_line] = data_change(line) #?체크
        combine_filedata = ''.join(file_data)
        print(combine_filedata)
        yield combine_filedata
