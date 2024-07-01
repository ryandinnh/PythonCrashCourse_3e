cities = ['chicago', 'new york city', 'boston', 'seattle', 'austin', 'san francisco', 'los angeles']

#adding additional cities
cities.append('charlotte')
cities.insert(0,'dc')

print(f"Cities: {cities}")

#removing cities
del cities[3] #remove 'boston'
cities.pop() #removes last city which is charlotte
cities.remove("austin")

print(f"\nUpdated city list: {cities}")

#sorting cities
cities.sort()
print(f"\nalphabetical sorted list: {cities}")

cities.sort(reverse=True)
print(f"\nreverse alphabetical sorted list: {cities}")

cities.reverse()
print(f"\nOriginal alphabetical order: {cities}")

#length of list
print(f"\nthe length of the list of cities is: {len(cities)}")
