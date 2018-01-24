#practice sorting list
places = ['Japan', 'Australia', 'Sweden', 'Canada', 'Grand Cayman']
for place in places:
    print(place)

#Now print sorted without changing actual list
print("Countries in sorted order: ")
print(sorted(places))

#or backwards
print("...and backwards")
print(sorted(places, reverse=True))

#reverse order of list
print(places)
places.reverse()
print(places)
places.reverse()
print("now back in order/t")
print (places)
