import sqlite3
from sqlite3 import Error
from datetime import datetime
import random

"""
필요한 것들

1. DB에서 오름차순으로 정렬후 데이터 가져오기
2. 가져온 데이터를 다시 웹캠에 보내기
"""

def create_connection(db_file):
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def print_db(conn,sql_input):
	try:
		c = conn.cursor()
		c.execute(sql_input)
		rows = c.fetchall()
		for row in rows:
			row_num = row[0]
	except Error as e:
		print(e)



def read_db(conn,num,row_num):
	sql_find = """SELECT COUNT(data) FROM FuzzingTable;"""
	try:
		c = conn.cursor()
		if num == 0:
			c.execute(sql_find)
			rows = c.fetchall()
			for row in rows:
				row_num = row[num]
				return row_num
		elif num == 3:
			skip = 0
			for i in range(0,row_num):
				win = random.randrange(0,4)
				if win == 0:
					break
				skip += 1
			sql_line = f"SELECT * FROM FuzzingTable order by code_coverage desc limit {skip}, 1;"
			c.execute(sql_line)
			rows = c.fetchall()
			for row in rows:
				lines = row[num]
				return lines
	except Error as e:
		print(e)

	
def main_db():
	row_num = 0 
	db_file = './test.db'
	conn = create_connection(db_file)
	row_num = read_db(conn,0,row_num)
	line_data = read_db(conn,3,row_num)
	print(line_data)
	yield line_data