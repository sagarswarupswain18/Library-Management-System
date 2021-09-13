import book_database
import student_database
from table_creation import *
import password_verification

db=SqliteDatabase('admin_table.db')
db.connect()

def main(id):
    print('\nWelcome to Admin_Module ')
    while(True):
        print('\n1.Add/ Delete/ Modify Books')
        print('2.Add/ Delete/ Modify Students')
        print('3.List books available in library')
        print('4.List of Students registered in Library')
        print('5.Change password ')
        print('6.Back')
        n=input('Enter your choice: ')
        if n=='1':
            book_database.main()
        elif n=='2':
            student_database.main()
        elif n=='3':
            book_database.display_details()
        elif n=='4':
            student_database.display_details()
        elif n=='5':
            f=0
            old=input('Please enter your old password ')
            for i in Acount:
                if i.username==id and i.password==old:
                    new=input('Enter your new password:')
                    p=password_verification.password_verification(new)
                    if p==1:
                        i.password=new
                        i.save()
                        print('Modified Successfully')
                        break
                    else:
                        print('Incorrect password type')
                        break
                    f=1
                if i.username==id and i.password!=old:
                    print('Wrong old password')

        elif n=='6':
            break
        else:
            print('\nWrong choice')