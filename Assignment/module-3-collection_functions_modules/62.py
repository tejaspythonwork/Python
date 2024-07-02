# calculate surface volume and area of cylinder
'''
volume_of_cylinder = pi * r * r *h
r - radius
h - height
-----------------------------------
area of cylinder = 2 * pi * r * h + 2 * pi * r * r

'''

import math

print('calculating area of cylinder')
radius = int(input('please enter radius'))
height = int(input('enter height: '))

volume = math.pi * radius * radius * height
print('--------------------------------------------------')
print(f'volume = {volume.__round__(2)}')

area = 2 * math.pi * radius * height + 2 * math.pi * radius * radius
print('--------------------------------------------------')
print(f'area = {area.__round__(2)}')