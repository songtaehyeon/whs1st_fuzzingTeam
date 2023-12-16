import sqlite3
from sqlite3 import Error
from datetime import datetime

# 데이터베이스 연결 생성
def create_connection(db_file):
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

# SQL 명령어 실행
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

# 테이블 삭제
def drop_table(conn):
    sql_drop_table = "DROP TABLE IF EXISTS FuzzingTable;"
    execute_sql(conn, sql_drop_table)

# 테이블 생성
def create_table(conn):
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS FuzzingTable(
        test_case_index INTEGER PRIMARY KEY,
        type TEXT,
        description TEXT,
        data BLOB,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_truncated BOOLEAN,
        code_coverage INTEGER
    );"""
    execute_sql(conn, sql_create_table)

# 예제 값 삽입
def insert_example_values(conn, data):
    sql_insert_values = """
    INSERT INTO FuzzingTable(test_case_index, type, description, data, timestamp, is_truncated, code_coverage) 
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    execute_sql(conn, sql_insert_values, data)

# 모든 row 출력
def select_all_rows(conn):
    sql_select_all = """SELECT * FROM FuzzingTable;"""
    try:
        c = conn.cursor()
        c.execute(sql_select_all)
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection("./test.db")
    drop_table(conn)
    create_table(conn)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    example_values = [(1, 'type1', 'description1', 'data1', now, 0, 20),
                      (2, 'type2', 'description2', 'data2', now, 0, 40),
                      (3, 'type3', 'description3', 'data3', now, 0, 60),
                      (4, 'type4', 'description4', 'data4', now, 0, 80),
                      (5, 'type5', 'description5', 'data5', now, 0, 100)]
    for data in example_values:
        insert_example_values(conn, data)
    select_all_rows(conn)
