print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Jayateja@1' and username=='Jayateja':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1
