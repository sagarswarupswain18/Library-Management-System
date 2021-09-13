import json
from peewee import *
from table_creation import *

db=SqliteDatabase('admin_table.db')
db.connect()

def display_all_data():
    with open('student_details.json') as f:
       data = json.load(f) 
    
    for i in range(0,len(data)):
        
        Student.create(name=data[i]['name'],sic=data[i]['sic'],phone=data[i]['phone'],email=data[i]['email'])

display_all_data()
print('\nData added successfully')