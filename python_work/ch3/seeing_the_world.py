destinations = ["japan", 'korea', 'vietnam', 'france', 'england'] #five places in the world id like to vists

print(destinations) #printing original list

#printing list in alphabetical order
print(f"\nAlphabetical sort of the list: {sorted(destinations)}")

print(f"Original order: {destinations}")

#reverse order
destinations.reverse()
print(f"\nThe reversed order of this list: {destinations}")
destinations.reverse()
print(f"Original order: {destinations}")

#alphabetical sorted order
destinations.sort()
print(f"\nAlphabetical sorted order: {destinations}")

#reverse alphabetical sorted order
destinations.sort(reverse=True)
print(f"\nReverse alphabetical sorted order: {destinations}")