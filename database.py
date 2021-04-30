import sqlite3
from sqlite3 import Error
import datetime

teachers_date = {'teacher1': '12345', 'teacher2': '67890', 'teacher3': '13579', 'teacher4': '24680'}

# if ('teacher1', 12345) in teachers_date.items():
#     print(1)

def get_orders_by_price(subject = 0, price = 0):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()

    a = cursor.execute('select * from teacher_table ').fetchall()

def find_in_cpp(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select date_of_start from cpp where students_id = ?', (id,)).fetchall()
    if len(a) > 0:
        return a
    else:
        return False
def find_in_java(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select date_of_start from java where students_id = ?', (id,)).fetchall()
    if len(a) > 0:
        return a
    else:
        return False
def find_in_python(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select date_of_start from python where students_id = ?', (id,)).fetchall()
    if len(a) > 0:
        return a
    else:
        return False
def find_in_sql(id: int):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select date_of_start from sql_ where students_id = ?', (id,)).fetchall()
    if len(a) > 0:
        return a
    else:
        return False

def find_in_students(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select * from students_table where id = ?', (id,)).fetchall()
    if len(a) > 0:
        return True
    else:
        return False

def add_to_students_table(id, name, second_name, surname):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    cursor.execute('insert into students_table ("id", "name", "second_name", "surname", '
                   '"python_hooky","java_hooky","sql_hooky","cpp_hooky") '
                   'values(?, ?, ?, ?, ?, ?, ?, ?)',(id,name, second_name, surname, 0,0,0,0))
    db.commit()

def add_to_cpp(id, date):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    cursor.execute('insert into cpp ("students_id", "scores", "date_of_start") values(?,?,?)', (id, 0, date)).fetchall()
    db.commit()

def add_to_java(id, date):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    cursor.execute('insert into java ("students_id", "scores", "date_of_start") values(?,?,?)', (id, 0, date)).fetchall()
    db.commit()
def add_to_sql(id, date):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    cursor.execute('insert into sql_ ("students_id", "scores", "date_of_start") values(?,?,?)', (id, 0, date)).fetchall()
    db.commit()
def add_to_python(id, date):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    cursor.execute('insert into python ("students_id", "scores", "date_of_start") values(?,?,?)', (id, 0, date)).fetchall()
    db.commit()

def get_scores_java(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select scores from java where students_id = ?', (id,)).fetchall()
    return a
def get_scores_python(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select scores from python where students_id = ?', (id,)).fetchall()
    return a
def get_scores_sql(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select scores from sql_ where students_id = ?', (id,)).fetchall()
    return a
def get_scores_cpp(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select scores from cpp where students_id = ?', (id,)).fetchall()
    return a
def get_all_java():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select * from java ').fetchall()
    return a

def get_all_cpp():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select * from cpp ').fetchall()
    return a
def get_all_python():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select * from python ').fetchall()
    return a
def get_all_sql():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select * from sql_ ').fetchall()
    return a
def ids_java():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select students_id from java ').fetchall()
    return a
def ids_cpp():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select students_id from cpp ').fetchall()
    return a
def ids_python():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select students_id from python ').fetchall()
    return a
def ids_sql():
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select students_id from sql_ ').fetchall()
    return a
def get_name(id):
    db = sqlite3.connect('botdatabase.db')
    cursor = db.cursor()
    a = cursor.execute('select "second_name", "name", "surname" from students_table ').fetchall()
    return a

print(get_name(719274325)[0][1])