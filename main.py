person = {
    'first_name' : 'bobby',
    'last_name' : 'mcneal',
    'age' : 47,
    'phone' : 123454321
}

person['nationality'] = 'American'

name = input("Enter name: ")
if person['first_name'] == name:
    print('')
    for key, value in person.items():
        print(key, ": ", value)
else:
    print(f"{name} not found.")