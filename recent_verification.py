from peewee import *
from table_creation import *

db=SqliteDatabase('admin_table.db')
db.connect()

def recent(sic):

    data=[]
    
    for i in book_issue:
        data.append(i.student_id)
  
    if len(data)>1:
        if data[len(data)-1]==sic and data[len(data)-2]==sic:
            return 1
        else:
            return 0
    else:
        return 0


