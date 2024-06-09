# area of square and circumference of circle 
# area_of_circle = pi * r * r
# circumference_circle = 2 * pi * r

import math as math

print('Finding area of circle')
r = float(input('Enter r'))
area_of_circle = math.pi * r * r
print(f'Area of circle = {area_of_circle.__round__(2)}')

print('--------------------------------------')
print('Finding circumference of circle')
circumference_circle = 2 * math.pi * r
print(f'Area of circle = {circumference_circle.__round__(2)}')