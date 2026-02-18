while True:
    
    username = str(input("Create a username: "))
    print(f"Username: {username}")
    response = input("Would you like to change your username? Please enter 'yes' or 'no': ").lower()
    
    if response == 'yes':
        username = str(input("Create a username: "))
        print(f"Username: {username}")
        response = input("Would you like to change your username? Please enter 'yes' or 'no': ").lower()
    
    if response == 'no':
        print(f'Your permanent username is: {username} ')
        break
