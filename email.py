import pickle
import sys
import os
from datetime import datetime
from time import strftime

environment_items = dict(**os.environ)
print ('\n' + environment_items['HOMEDRIVE'] + environment_items['HOMEPATH'])
now = datetime.now()
print('%s/%s/%s' % (now.month, now.day ,now.year) + (now.strftime(' %I:%M:%S %p' )) + '\n')

def main():

    try:
        f = open('email.dat','rb')
        d = pickle.load(f)
        f.close()
        
    except:  
        d = {}

    while True:

        print('\nMenu')
        print('------------------------------')
        print('1. Find a email address')
        print('2. Add name and email address')
        print('3. Change an exsiting email address')
        print('4. Delete a name and email address')
        print('5. Quit the program\n')

        choice = input('Enter a choice: ')

        if choice:
            choice=int(choice)
        else:
            print('\nEnter a number:')
            continue  

        if choice == 1:

            while True:

                name = input('Enter a name: ')

                if name:
                    if name in d:
                        print('\nName:%s\nEmail:%s' % (name,d[name]))
                        break
                    else:
                        print('Email not found')
                        break
                else:
                    print('Name cannot be empty')
                    continue
            
        elif choice == 2:

            while True:          
        
                name = input('Enter a name: ')

                if name:
                    break
                else:
                    print('Name cannot be empty ')
                    continue

            while True:          
        
                email = input('Enter the email address: ')

                if email:
                    d[name] = email
                    print('Name and address have been added')
                    break
                else:
                    print('Email cannot be empty')
                    continue
            
        elif choice == 3:

            while True:          
        
                name=input('Enter a name: ')

                if name:
                    if name in d:
                        email = input('Enter the new email address: ')
                        d[name] = email
                        print('Information updated')
                        break;
                    else:
                        print('Name not found')
                        break
                else:
                    print('Name cannot be empty')
                    continue
            
        elif choice == 4:

            while True:          
        
                name=input('Enter the name to remove: ')

                if name:
                    if name in d:
                        del d[name]
                        print('Information deleted')
                        break;
                    else:
                        print('Name not found ')
                        break
                else:
                    print('Name cannot be empty')
                    continue

        elif choice == 5:
        
            f=open('email.dat','wb')
            pickle.dump(d,f)
            f.close()
            print('Information Saved')
            sys.exit()
        else:
            print('\nEnter a valid choice ')
main()
