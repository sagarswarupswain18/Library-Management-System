from peewee import *
from table_creation import *

db=SqliteDatabase('admin_table.db')
db.connect()

def display_details():
    print('\nPrinting the list of books present in the library: ')
    print('-'*130)
    print('{:>3} {:>27} {:>31} {:>30} {:>23}'.format('Id','Book_Name','Author_Name','Copies','Availability'))
    print('-'*130)
    for i in Books:
        if i.no_of_books==0:
            print('{:<20} {:<30} {:<30} {:>10} {:>25}'.format(i.book_id,i.book_name,i.author_name,i.no_of_books,'Not Available'))
        else:
            print('{:<20} {:<30} {:<30} {:>10} {:>25}'.format(i.book_id,i.book_name,i.author_name,i.no_of_books,'Available'))
    print('\n')

def add_book():
    name=input('Enter the name of the book: ')
    while(True):
        f=0
        n=input('Enter the book id: ')
        for i in Books:
            if n==i.book_id:
                print('Book id already present: ')
                f+=1
        if f==0:
            si=n
            break

    ph=input('Enter the author name: ')

              
        
    while(True):
        em=int(input('Enter the number of copied of the book present in the library: '))
        if em>=0:
            count=em
            break
        else:
            print('Wrong input\n')
    Books.create(book_name=name,book_id=si,author_name=ph,no_of_books=count)
    print('Book details added successfully: ')

def modify_book():
    f=0
    n=input('Enter the book id you wants to modify :')
    for i in Books:
        if i.book_id==n:
            f=1
            print('Enter the part you wants to modify of the student: ')
            print('\n1.Book Name\n2.Author name\n3.No of copies\n4.Book id\n5.Back')
            n=input('Enter your choice: ')
            if n=='1':
                name=input('Enter the modified name: ')
                i.book_name=name
                i.save()
                print('Modified successfully: ')
            elif n=='2':
                author=input('Enter the modified author name: ')
                i.author_name=author
                i.save()
                print('Modified successfully: ')
                break
            elif n=='3':
                while(True):
                    em=int(input('Enter the number of copied of the book present in the library: '))
                    if em>=0:
                        i.no_of_books=em
                        i.save()
                        print('Modified successfully: ')
                        break
                    else:
                        print('Wrong input\n')
            elif n=='4':
                while(True):
                    j = 0
                    idr = input('enter the book id: ')
                    for t in Books:
                        if t.book_id== idr:
                            print('sorry!! the book id already exists\n try again!!')
                            j = 1
                    if j == 0: 
                        i.book_id = idr
                        i.save()
                        print('Modified successfully:')
                        break 
            elif n=='5':
                break
            else:
                print('Wrong input of your choice: ')
    if f==0:
        print('Match not found: ')

def delete_book():
    f=0
    n=input('Enter the id of the book you wants to delete: ')
    for i in Books:
        if i.book_id==n:
            f=1
            i.delete_instance()
            print('Deleted successfully: ')
    if f==0:
        print('Match not found: ')

def main():
    while(True):
        print('\n1.Add Book\n2.Modify Book\n3.Delete Book\n4.Back')
        n=input('Enter your choice: ')
        if n=='1':
            add_book()
        elif n=='2':
            modify_book()
        elif n=='3':
            delete_book()
        elif n=='4':
            break
        else:
            print('\nWrong input')

