#First things first: Type the coordinates from both cities in the screen.
import math
try:
    lat_1 = float(input('Enter with the latitude from the 1° city:'))
    long_1 = float(input('Now enter with the longitude from this same city:'))
    lat_2 = float(input('Inform the latitude from 2° city:'))
    long_2 = float(input("And finally, the 2° city's longitude:"))
except ValueError:
    print('Sorry, only numbers are allowed. Please enter the coordinates again:')
#Then, we must convert the latitude and longitude values from decimal degrees to radians.
lat_1 = math.radians(lat_1)
long_1 = math.radians(long_1)
lat_2 = math.radians(lat_2)
long_2 = math.radians(long_2)
#Now we going to use the so-called Haversine formula:
dlat = lat_2 - lat_1
dlong = long_2 - long_1
dist = 2 * math.asin(math.sqrt(math.sin(dlat/2)**2 + math.cos(lat_1) * math.cos(lat_2) * math.sin(dlong/2)**2))
#After this, we must multiply the result by 6371 if we want the result in miles, or by 3956 if we prefer using kilometers.
radius_mi = 6371
radius_km = 3956
dist_mi = dist * radius_mi
dist_km = dist * radius_km
#At last, we'll show two options: Show the distance in miles or show it in kilometers.
#We should print the menu:
print('''Show the distance in:
    [1] Miles
    [2] Kilometers''')
#Then the answer to the user's choice:
option = int(input('Which do you prefer? '))
if option == 1:
    print(f'''
    The distance between the two cities is {dist_mi.__round__(2)} mi.''')
    pass
elif option == 2:
    print(f'''
    The distance between the two cities is {dist_km.__round__(2)} km.''')
    pass
else:
    print("""
    This option isn't among the alternatives. Please choose a correct number.""")
#And that's it. Simple, isn't?
