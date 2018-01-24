#store a list of names and then print them
names = ['Kurt', 'Jenn', 'Lexi', 'Lucas', 'Scout']
for name in names:
    print(name)

#now print a greeting for each

for name in names:
    print("Hello " + name + ", how are you today?")

#now append some folks
names.append('Ashley')
print(names[5] + "is the most recent addition to the list")

#insert Jeff
names.insert(5,'Jeff')
print(names[5] + " is the most recent addition to the list")

#now remove Jeff
del names[5]
for name in names:
    print("Hello " + name + ", how are you today?")

#now try pop method
pet = names.pop()
print("The person popped from the list is " + pet)

#Now let's remove the pet
names.remove('Scout')
print("After using Remove method on Scout, Remaining names are:")
for name in names:
    print(name)
