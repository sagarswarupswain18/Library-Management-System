import main
import librarian_module

def main_menu():
    while(True):
        print('\n1.Admin Login')
        print('2.Librarian login')
        print('3.Exit')
        n=input('Enter your choice')
        if n=='1':
            main.main()
        elif n=='2':
            librarian_module.main()
        elif n=='3':
            exit()
        else:
            print('\nWrong choice')
    
main_menu()