# wap to accept height of person in centimeter
# categories person accordingly their height
# short - [150,155] average - [165,170] tall - [180,190]

height = int(input('Please enter your height in c.m. : '))
short = [150,155]
average = [165,170]
tall = [180,190]

def category_heights():
    global height
    if height < 160:
        if height not in short:
            print('-----')
            print('Short')
            print('-----')
    elif 160 <= height < 180:
        if height not in average:
            print('Average')
    else:
        if height not in tall:
            print('tall') 

category_heights()                         


            