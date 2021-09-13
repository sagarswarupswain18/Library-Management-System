from peewee import *
db=SqliteDatabase('admin_table.db')

class Student(Model):
    name=CharField()
    sic=CharField()
    phone=IntegerField()
    email=CharField()
    class Meta:
        database=db
class Books(Model):
    book_id=CharField()
    book_name=CharField()
    author_name=CharField()
    no_of_books=IntegerField()
    class Meta:
        database=db

class Acount(Model):
    username = CharField()
    password = CharField()
    name = CharField()
    class Meta:
        database = db

class book_issue(Model):
    book_id=CharField()
    student_id=CharField()
    class Meta:
        database=db

# class Is
db.connect()
db.create_tables([Student,Books,Acount,book_issue])
#print('Table created successfully: ')
#p=Student.create(name='sagar',sic='80310076',phone=154,email='sagar@gmail.com')