from peewee import *
from table_creation import *

db=SqliteDatabase('admin_table.db')
db.connect()

def student_id(id):
    for i in Student:
        if id==i.sic:
            return 1
    return 0

def book_id(id):
    for i in Books:
        if id==i.book_id:
            return 1
    return 0

