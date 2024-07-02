# to check that triangle can formed with 
# given values for angels

def triangle():
    angle1 = int(input('Please enter first angle'))
    angle2 = int(input('Please enter first angle'))
    angle3 = int(input('Please enter first angle'))

    if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
        return True
    else:
        return False
    

if triangle():
    print('Triangle Can Be Formed')
else:
    print('Triangle Can Not Be Formed')

