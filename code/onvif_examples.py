import os
import random
import string

def data_change(input_data):
	for i in range(10):
		input_data.replace("?",''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace)for j in range(random.randint(5, 50))))
	print(input_data)

def read_data(data):
	for file_line in range(len(data)):
		if "?" in data[file_line]:
			data_change(data[file_line])

data_folder = "../extract_data/split"
file_list = os.listdir(data_folder)

for file_num in range(1):
	files = file_list[file_num] if file_list else None

	if files:
		file_path = os.path.join(data_folder,files)
		with open(file_path) as file:
			data = file.readlines()
			read_data(data)
	else:
		print("NOPE")