import os
import random
import string

#랜덤한 인풋 데이터로 만들기
def random_input(file_data):
    for file_line in range(len(file_data)):
        input_line = file_data[file_line]
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
        file_data[file_line] = output_line
    combine_filedata = ''.join(file_data)
    return combine_filedata

#패킷 순서 변환 (미완)
def shuffle_list(file_data):
    if type(file_data) == str:
        file_data = file_data.splitlines()
    random.shuffle(file_data)
    combine_filedata = ''.join(file_data)
    return combine_filedata

#soap에 태그중에 하나를 랜덤하게 고른뒤 랜덤하게 태그를 바꿔보기 
def change_tag(file_data,file_tag,total_tag):
    target_tag = random.choice(file_tag) #실제 파일에 있는 태그 
    random_tag = random.choice(total_tag) # 바꿀 태그선택
    output_line = """"""
    if target_tag == random_tag:
        change_tag(file_data,file_tag, total_tag)
    else:
        for file_line in file_data:
            find_tag = file_line.rfind(target_tag)
            if find_tag == -1:
                output_line += file_line
            else:
                new_line = file_line.replace(target_tag,random_tag)
                output_line += new_line
        return output_line


#soap에 태그중에 하나를 랜덤하게 고른뒤 태그를 없애보기
def del_tag(file_data, file_tag):
    # 무작위로 태그 하나를 선택합니다.
    random_tag = random.choice(file_tag)

    # 선택된 태그가 포함된 라인의 인덱스를 찾습니다.
    tag_line_indices = [i for i, line in enumerate(file_data) if random_tag in line]

    # 태그가 포함된 라인이 없으면, 원본 데이터를 그대로 반환합니다.
    if not tag_line_indices:
        return ''.join(file_data)

    # 태그가 포함된 라인 중 하나를 무작위로 선택하여 제거합니다.
    del_index = random.choice(tag_line_indices)
    del file_data[del_index]

    # 수정된 데이터를 문자열로 결합하여 반환합니다.
    return ''.join(file_data)

#정말 랜덤한 위치부터 랜덤한 길이로 랜덤한 문자열 보내보기
def random_location(file_data):
    combine_filedata = ''.join(file_data)
    input_location = random.randrange(0,len(combine_filedata))
    random_str = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(5, 50)))
    new_filedata = combine_filedata[:input_location]+random_str+combine_filedata[input_location:]
    return new_filedata

#태그를 수집하기
def soap_parse(file_data,total_tag):
    file_data = file_data
    tags = []
    for file_line in file_data:
        i = 0
        while i < len(file_line):
            if file_line[i] == '<' and i+1 < len(file_line) and file_line[i+1] == '/':
                tag_start = i + 2 
                i += 2 
                while i < len(file_line) and file_line[i] != '>':
                    i += 1
                if i < len(file_line):
                    tag_content = file_line[tag_start:i] 
                    tags.append(tag_content)
            i += 1
    for tag in tags:
        if tag not in total_tag:
            total_tag.append(tag)
    return tags,total_tag

def soap_parse_DB(file_data,total_tag):
    tags = []
    for file_line in file_data:
        i = 0
        while i < len(file_line):
            if file_line[i] == '<' and i+1 < len(file_line) and file_line[i+1] == '/':
                tag_start = i + 2 
                i += 2 
                while i < len(file_line) and file_line[i] != '>':
                    i += 1
                if i < len(file_line):
                    tag_content = file_line[tag_start:i] 
                    tags.append(tag_content)
            i += 1
    for tag in tags:
        if tag not in total_tag:
            total_tag.append(tag)
    return tags,total_tag

#파일 읽기
def process_file(file_path,total_tag):
    with open(file_path, 'r') as file:
        file_data = file.readlines() #파일안의 내용이 리스트로 나옴
        file_tag , total_tag = soap_parse(file_data,total_tag)
        choices = random.randrange(0, 5)
        marge_data = []
        if choices == 0:
            data = random_input(file_data)
            marge_data.append(data)
            marge_data.append(total_tag)
            return marge_data
        elif choices == 1:
            data = shuffle_list(file_data)
            marge_data.append(data)
            marge_data.append(total_tag)
            return marge_data
        elif choices == 2:
            data = change_tag(file_data, file_tag , total_tag)
            marge_data.append(data)
            marge_data.append(total_tag)
            return marge_data
        elif choices == 3:
            data = del_tag(file_data, file_tag)
            marge_data.append(data)
            marge_data.append(total_tag)
            return marge_data
        else:
            data = random_location(file_data)
            marge_data.append(data)
            marge_data.append(total_tag)
            return marge_data

def process_db(db_data,total_tag):
    file_data = db_data
    file_tag , total_tag = soap_parse_DB(file_data,total_tag)
    choices = random.randrange(0, 4)
    marge_data = []
    if choices == 0: 
        data = shuffle_list(file_data)
        marge_data.append(data)
        marge_data.append(total_tag)
        return marge_data
    elif choices == 1: 
        data = change_tag(file_data, file_tag , total_tag)
        marge_data.append(data)
        marge_data.append(total_tag)
        return marge_data
    elif choices == 2:
        data = del_tag(file_data, file_tag)
        marge_data.append(data)
        marge_data.append(total_tag)
        return marge_data
    else:
        data = random_location(file_data)
        marge_data.append(data)
        marge_data.append(total_tag)
        return marge_data




