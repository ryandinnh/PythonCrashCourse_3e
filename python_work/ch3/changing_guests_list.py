guests = ['mom','dad','brother','grandma','cousin'] #list of og guests

#for loop to invite each guests
"""
for name in guests:
    print(f"Dear {name.title()}, you are invited to the party!")
"""
missed_guest = 'mom'
new_invite = 'uncle'

#list.index(value) finds the index of an item in a list, use this to record the index of where we want to put the new invite
missed_guest_index = guests.index(missed_guest)
guests.remove(missed_guest)
guests.insert(missed_guest_index, new_invite)

#printing missed guests
print(f"Sorry {missed_guest.title()}, could not make the party.")

#printing guests
for name in guests:
    print(f"Dear {name.title()}, you are invited to the party!")
