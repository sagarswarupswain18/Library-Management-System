from peewee import *
import email_varification
import phone_varification
from table_creation import *


db=SqliteDatabase('admin_table.db')
db.connect()

def display_details():
    print('\nPrinting the list of student registered in the library: ')
    print('-'*100)
    print('{:>3} {:>25} {:>28} {:>25}'.format('Sic','Name','Phone','Email'))
    print('-'*100)
    for i in Student:
        print('{:<20} {:<30} {:<20} {:>6}'.format(i.sic,i.name,i.phone,i.email))
    print('\n')

def add_student():
    name=input('Enter the name of the student: ')
    while(True):
        f=0
        n=input('Enter the sic of the student: ')
        for i in Student:
            if n==i.sic:
                print('sic should be unique: ')
                f+=1
        if f==0:
            si=n
            break

    while(True):
        ph=int(input('Enter the phone number of the student: '))
        l=phone_varification.phone_varification(ph)
        if l==1:
            phone_no=ph
            break
        else:
            print('Wrong input\n')           
        
    while(True):
        em=input('Enter the email of the student: ')
        l=email_varification.email_varification(em)
        if l==1:
            mail=em
            break
        else:
            print('Wrong input\n')
    Student.create(name=name,sic=si,phone=phone_no,email=mail)
    print('Student details added successfully: ')

def modify_student():
    f=0
    n=input('Enter the sic you wants to modify :')
    for i in Student:
        if i.sic==n:
            f=1
            print('Enter the part you wants to modify of the student: ')
            print('\n1.Name\n2.Phone\n3.Email\n4.Student sic\n5.Back')
            n=input('Enter your choice: ')
            if n=='1':
                name=input('Enter the modified name: ')
                i.name=name
                i.save()
                print('Modified successfully: ')
            elif n=='2':
                while(True):
                    phone=int(input('Enter the modified phone: '))
                    p=phone_varification.phone_varification(phone)
                    if p==1:
                        i.phone=phone
                        i.save()
                        print('Modified successfully: ')
                        break
                    else:
                        print('Wrong input of phone number: ')
            elif n=='3':
                while(True):
                    em=input('Enter the email of the student: ')
                    l=email_varification.email_varification(em)
                    if l==1:
                        i.email=em
                        i.save()
                        print('Modified successfully: ')
                        break
                    else:
                        print('Wrong input\n')
            elif n=='4':
                while(True):
                    j = 0
                    si = input('enter the sic of the student:')
                    for t in Student:
                        if t.sic == si:
                            print('sorry!! the student id already exists')
                            j = 1
                    if j == 0:
                        i.sic = si
                        i.save()
                        print('Modified successfully:')
                        break
            elif n=='5':
                break
            else:
                print('Wrong input of your choice: ')
    if f==0:
        print('Match not found: ')

def delete_student():
    f=0
    n=input('Enter the sic of the student you wants to delete: ')
    for i in Student:
        if i.sic==n:
            f=1
            i.delete_instance()
            print('Deleted successfully: ')
    if f==0:
        print('Match not found: ')

def main():
    while(True):
        print('\n1.Add Student\n2.Modify Student\n3.Delete Student\n4.Back')
        n=input('Enter your choice: ')
        if n=='1':
            add_student()
        elif n=='2':
            modify_student()
        elif n=='3':
            delete_student()
        elif n=='4':
            break
        else:
            print('Wrong input')

