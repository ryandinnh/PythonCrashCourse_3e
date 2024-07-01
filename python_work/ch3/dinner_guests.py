guests = ['mom','dad','brother','grandma','cousin'] #list og guests

#for loop to invite each guests
for name in guests:
    print(f"Dear {name.title()}, you are invited to the party!")

print(f"\nThe total number of guests invited is: {len(guests)} guests")