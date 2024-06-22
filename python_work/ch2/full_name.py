first_name='ada'
last_name='lovelace'
full_name = f'{first_name} {last_name}' #f denotes f-strings which let you use variable values inside a string
print(full_name)

print(f"Hello, {full_name.title()}!") #can still call methods on variables inside the string