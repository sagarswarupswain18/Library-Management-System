from peewee import *
from table_creation import *
import password_verification
import getpass
import admin_module

db=SqliteDatabase('admin_table.db')
db.connect()

def main():
    while(True):
        print('\n1.Create new account:')
        print('2.Log in:')
        print('3.Back:')
        n=input('Enter your choice:')
        if n=='1':
            while(True):
                c=0
                usr = input('enter your user id (9 digits employee id)')
                if len(usr)!= 9:
                    print('Incorrect username type:')
                    break
                for i in Acount:
                    if i.username==usr:
                        c=1
                        break
                if c==1:
                    print('Account already exits: ')
                    break
                pas = input('enter password')
                p=password_verification.password_verification(pas)
                if p==0:
                    print('Incorrect password type: ')
                    break
                nm = input('enter the name')
                Acount.create(username = usr, password = pas , name = nm )
                print('thank you your account is created!!!')
                break

        elif n=='2':
            found = True
            while found:
                chk_pas = 0
                chk_usr = 0
                nme = input('enter your username')
                for acc in Acount.select():
                    if acc.username == nme:
                        found = False
                        chk_usr = 1
                        break
                if chk_usr == 0:
                    print('sorry the account doesnot exists')
                    break
                while (True):
                    cnt = 1
                    while cnt <= 3:
                        
                        pasw = getpass.getpass(prompt = 'enter your password')
                        if acc.password == pasw:
                            chk_pas = 1
                            break
                        else:
                            print('wrong password!! please try again')
                            cnt +=1
                    if cnt == 4:
                        print('sorry too many unsuccessfull attempts')
                        break
                    break
                if chk_usr == 1 and chk_pas == 1:
                    print('\nwelcome Mr./Mrs. ',acc.name)
                    admin_module.main(acc.username)
        elif n=='3':
            break
        else:
            print('Wrong choice')
