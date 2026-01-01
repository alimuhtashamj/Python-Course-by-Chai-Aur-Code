# Create a function that returns both the area and 
# circumference of a circle given its RADIUS.
import math 
def func(radius):
    area = math.ceil((math.pi * radius ** 2))
    circumfrence = math.ceil(2*math.pi*radius**2)
    return area, circumfrence

a,c = func(2)
print('Area:',a,'Circumfrence:',c)
