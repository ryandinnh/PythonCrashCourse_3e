import random #used to generate a random int value

age = random.randint(0,100) #random int value between 0 and 100 inclusive

if age <2:
    print("This person is a baby")
elif 2<=age<4:
    print("This person is a toddler")
elif 4 <= age < 13:
    print("This person is a kid")
elif 13 <= age < 20:
    print("This person is a teenager")
elif 20 <= age < 65:
    print("This person is an adult")
else:
    print("This person is an elder")

print(f"This person's age is: {age}")