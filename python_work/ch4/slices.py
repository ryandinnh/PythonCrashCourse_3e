numbers = list(range(0,21)) #list of 0,20 inclusive

print(f"The first three numbers in the list are: {numbers[:3]}\n")

print(f"Three items from the middle of the list are: {numbers[int((len(numbers)/2)-1):int((len(numbers)/2)+2)]}\n") #needs to be +2 at the end value because the index is -1

print(f"The last three items in the list are: {numbers[-3:]}")
