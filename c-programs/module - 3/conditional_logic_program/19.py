# calculate and print electricity bill of customer
# info - customer id - name - unit consumed

print('Accepting Electricity Bill Information')
name = input('Please enter customer name: ')
customer_id = int(input('Please enter customer ID: '))
units = int(input('Please enter units consumed: '))

def calculateUnitsCharge():
    if units <=350:
        return 1.20
    elif units >= 350 and units <600:
        return 1.50
    elif units >= 600 and units <800:
        return 1.80
    elif units >= 800:
        return 2.00
    

calculateBill = calculateUnitsCharge()
print(calculateBill) 
   