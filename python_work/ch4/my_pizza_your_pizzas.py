pizzas = ['pepperoni', 'sausage','hawaiian']
friend_pizzas = pizzas[:]

pizzas.append('cheese')
friend_pizzas.append('chicken')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)