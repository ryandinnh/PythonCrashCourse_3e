guests = ['mom','dad','brother','grandma','cousin'] #list og guests

#for loop to invite each guests
for name in guests:
    print(f"Dear {name.title()}, you are invited to the party!")

print("Good news, we have more space at the table now! \nThe new invite list: ")

guests.insert(0, "Uncle")

#len() provides length of a list use it to find length of guests and divide by 2 ie middle of the list
guests.insert(int(len(guests)/2), 'aunt') #was an error here because div cast as a float need to cast as int. Also when length of list is even theres no actual middle (x.5 value)

guests.append('sister')

#for loop to invite each guests
for name in guests:
    print(f"Dear {name.title()}, you are invited to the party!")

print("\nOnly two guests can be invited now, unfortunately.\n")

#while loop to pop invitees until theres only 2
while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed.title()}, you have been removed from the guest list.")

#for loop to print guests still invited
for name in guests:
    print(f"Dear {name.title()}, congrats you are still invited to the party!")

""" Note this didnt work because i was modifying guests while iterating over it
#for loop to delete all guests in list
for name in guests:
    del guests[guests.index(name)]
"""

#.clear() also removes all items in a list
guests.clear()

print(guests)