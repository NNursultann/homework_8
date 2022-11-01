import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)

    return conn

def create_table(conn,sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_student(conn, student):
    try:
        sql = '''INSERT INTO students
        (fullname,mark,hobby,birth_date,is_married)
        VALUES (?,?,?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def delete_student(conn, id):
    try:
        sql = '''DELETE FROM students WHERE ID = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id, ))
        conn.commit()
    except Error as e:
        print(e)

def update_student_mark_and_martial_status(conn, student):
    try:
        sql = '''UPDATE students SET mark = ? ,is_married = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def select_all_student(conn):
        try:
            sql = '''SELECT * FROM students'''
            cursor = conn.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            for row in rows:
                print(row)

        except Error as e:
            print(e)

connection = create_connection(r'gr_23_3.db')
create_students_table ='''
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (200) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''

if connection is not None:
    print('Connected successfuly!')
    # create_table(connection, create_students_table)
    # create_student(connection,('Esen Mambetov',20.56,'Chess','2003-06-08',False))
    # create_student(connection,('Alex Brilliant',77.12,'','1989-12-31',True))

     # delete_student(connection, 3)
    # update_student_mark_and_martial_status(connection, (15.08,False,5))
    select_all_student(connection)

    print('Done!')
