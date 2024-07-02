# input electriccity unit charges
# and calculate total electricity bill


def calculate_electricity_bill():
    units = int(input('Enter Units: '))
    if units >=0 and units <=50:
        return 0.50
    if units >50 and units <=100:
        return 0.75
    if units >100 and units <=200:
        return 1.20
    else:
        return 1.50
    

unit = calculate_electricity_bill()
print(unit)    
    