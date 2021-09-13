import json
from peewee import *
from table_creation import *

db=SqliteDatabase('admin_table.db')
db.connect()

def display_all_data():
    with open('book_details.json') as f:
       data = json.load(f) 
    
    for i in range(0,len(data)):
        
        Books.create(book_id=data[i]['id'],book_name=data[i]['name'],author_name=data[i]['author'],no_of_books=data[i]['copies'])

display_all_data()
print('\nData added successfully')