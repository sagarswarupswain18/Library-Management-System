from peewee import *
from table_creation import *
import book_database
import student_database
import id_varificarion
import recent_verification



db=SqliteDatabase('admin_table.db')
db.connect()

def main():
    print('\nWelcome to librarian module ')
    while(True):
        print('\n1.List of book available in library: ')
        print('2.Issue book to student: ')
        print('3.Return book: ')
        print('4.List of book assigned: ')
        print('5.List of student having books: ')
        print('6.Back: ')
        n=input('Enter your choice: ')

        if n=='1':
            book_database.display_details()


        elif n=='2':
            f=0
            id=input('Enter the sic of the student: ')
            p=id_varificarion.student_id(id)
            if p==0:
                print("Sic doesn't match: ")
                continue
            p1=recent_verification.recent(id)
            if p1==1:
                print('\nYou have taken book continuesly 2 times\nTry again later\n')
                continue            
            id2=input('Enter the book id you wants to issue: ')
            p=id_varificarion.book_id(id2)
            if p==0:
                print("\nBook id does't match: ")
                continue
            for i in Books:
                
                if i.book_id==id2:
                    if i.no_of_books==0:
                        f=1

            if f==1:
                print('\nBook is currently not available in library: ')
                continue
            else:
                f=0
                for i in book_issue:
                    if i.book_id==id2 and i.student_id==id:
                        f=1
                if f==1:
                    print('\nYou have taken the same book already: ')
                    continue
                for i in Books:
                
                    if i.book_id==id2:
                        i.no_of_books-=1
                        i.save()
                book_issue.create(book_id=id2,student_id=id)
                print('\nBook issued Successfully: ')


        elif n=='3':
            f=0
            id=input('Enter the sic of the student: ')     
            id2=input('Enter the book id you wants to return: ')
            for i in book_issue:
                if i.student_id==id and i.book_id==id2:
                    f=1
                    for j in Books:
                        if j.book_id==id2:
                            j.no_of_books+=1
                            j.save()
                    i.delete_instance()
                    print('\nBook return successfully: ')
                    continue
            if f==0:
                print('\nSic or book id incorrect')
                continue 

        elif n=='4':
            print('\n1.Print specific book assign: ')
            print('2.Print all books assign: ')
            print('3.Back')
            n=input('Enter your choice: ')
            if n=='1':
                data=[]
                name=[]
                id2=input('Enter the id of the book you wants to check: ')
                p=id_varificarion.book_id(id2)
                if p==0:
                    print("\nBook id not present in library: ")
                    continue
                for i in book_issue:
                    if i.book_id==id2:
                        if i.student_id not in data:
                            data.append(i.student_id)
                for j in Student:
                    for i in data:
                        if j.sic==i:
                            name.append(j.name)
                print('List of student having book under book id:-',id2,'are:')
                print('-'*50)
                print('{:>3} {:>23}'.format('student_id','Student_names'))
                print('-'*50)
                for i in range(len(data)):
                    print('{:<20} {:<50}'.format(data[i],name[i]))
                
            elif n=='2':
                print('\nPrinting list of book assign: ')
                data2=[]
                for i in book_issue:
                    if i.book_id not in data2:
                        data2.append(i.book_id)
               
               # print(data2)
               
                for i in range(len(data2)):
                    print('\nList of student having book under book id:-',data2[i],'are:')
                    print('-'*50)
                    print('{:>3} {:>23}'.format('student_id','Student_names'))
                    print('-'*50)
                    data=[]
                    name=[]
                    for k in book_issue:
                        if k.book_id==data2[i]:
                            if k.student_id not in data:
                                data.append(k.student_id)
                    for j in Student:
                        for i in data:
                            if j.sic==i:
                                name.append(j.name)
                
                    for i in range(len(data)):
                        print('{:<20} {:<50}'.format(data[i],name[i]))
            
            elif n=='3':
                continue
            else:
                print('Wrong input: ')
        
        elif n=='5':
            print('\n1.Print specific student: ')
            print('2.Print all student with book name: ')
            print('3.Exit')
            n=input('Enter your choice: ')
            if n=='1':
                data=[]
                name=[]
                id2=input('Enter the sic of the student you wants to check: ')
                p=id_varificarion.student_id(id2)
                if p==0:
                    print("\nStudent not registered in library: ")
                    continue
                for i in book_issue:
                    if i.student_id==id2:
                        if i.book_id not in data:
                            data.append(i.book_id)
                for j in Books:
                    for i in data:
                        if j.book_id==i:
                            name.append(j.book_name)
                print('List of book with student id:-',id2,'are:')
                print('-'*50)
                print('{:>3} {:>23}'.format('Book_id','Book_names'))
                print('-'*50)
                for i in range(len(data)):
                    print('{:<20} {:<50}'.format(data[i],name[i]))
                
            elif n=='2':
                print('\nPrinting list of book assign: ')
                data2=[]
                for i in book_issue:
                    if i.student_id not in data2:
                        data2.append(i.student_id)
               
                #print(data2)
               
                for i in range(len(data2)):
                    print('\nList of book under student id:-',data2[i],'are:')
                    print('-'*50)
                    print('{:>3} {:>23}'.format('Book_id','Book_names'))
                    print('-'*50)
                    data=[]
                    name=[]
                    for k in book_issue:
                        if k.student_id==data2[i]:
                            if k.book_id not in data:
                                data.append(k.book_id)
                    for j in Books:
                        for i in data:
                            if j.book_id==i:
                                name.append(j.book_name)
                
                    for i in range(len(data)):
                        print('{:<20} {:<50}'.format(data[i],name[i]))
            
            elif n=='3':
                continue
            else:
                print('Wrong input: ')
        
        elif n=='6':
            break
        else:
            print('\nWrong choice')

#main()