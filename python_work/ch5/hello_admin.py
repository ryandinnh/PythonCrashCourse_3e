#includes no users mod too
#usernames = ['ryan', 'jaden', 'nolan', 'admin', 'roxas']
usernames =[]

if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello Admin, would you like to see a status report?\n")
        else:
            print(f"Hello {name.title()}, thank you for logging in again.\n")
else:
    print("We need to find more users!")