# find area of rectangle prism formula
# a = 2(wl+hl+hw)
print('Find Area Of Rectangle Prism Formula')

length_p = float(input('Enter length'))
width_p = float(input('Enter width'))
height_p = float(input('Enter height'))

first = width_p * length_p
second = height_p * length_p
third = height_p * width_p
sum = first + second + third

area_rect_prism = 2 * sum
print(f'Area Of Rectangle Prism Formula {area_rect_prism}')