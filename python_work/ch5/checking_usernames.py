current_users = ['ryan', 'jaden', 'nolan', 'admin', 'roxas']

new_users = ['ryan', 'jaden', 'sora', 'henry', 'quynh']

#convert all items to lowercase for current users to cross check
current_users = [name.lower() for name in current_users]

for name in new_users:
    if name.lower() in current_users:
        print(f"{name.title()}, this username is already in use. Please make a new username.\n")
    else:
        print(f"{name.title()}, this username is available. Thanks for logging in!\n")