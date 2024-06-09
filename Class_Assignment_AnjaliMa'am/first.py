# This file contains code based on  / If - condition / input / variables 
# Inputs - 1. name 2.gender 3.age 4.product name 5.product weight(grams)
# mini project - name - Kalyan Jwellers - Task 3
'''--------------------------------------------------------------------------------------------------------------'''
name = input('Enter Your Name ')
gender = input('Enter Your Gender ').lower()
age = int(str(input('Enter Your age ')))
product_name = input('Enter Product Name ')
product_quantity = int(str(input('Enter Product Quantity - (In grams) ')))



# making charges
making_charges = 845
# gold rate per grams
gold_rate_per_gram = 5000
# total gold charges
total_gold_charges = product_quantity * gold_rate_per_gram

total_making_charges = making_charges * product_quantity
net_amount = total_making_charges + total_gold_charges
discounted_amount = 0


if gender == 'male':
    print('You are male')
    if age >= 65:
        if net_amount >= 200000 and net_amount < 300000:
            discount_in_percentage = 20
            print('between 2lkh and 3lkh-disc 20%')
            
            discounted_amount = (total_gold_charges * 20)/100
        elif net_amount >= 300000 and net_amount < 400000:
            discount_in_percentage = 30
            print('between 3lkh and 4lkh')    
            discounted_amount = (total_gold_charges * 30)/100

        elif net_amount >= 400000 and net_amount < 500000:
            discount_in_percentage = 35
            discounted_amount = (total_gold_charges * 35)/100

            print('between 4lkh and 5lkh') 
    else:        
        if net_amount >= 200000 and net_amount < 300000:
            discount_in_percentage = 10
            print('between 2lkh and 3lkh')
            discounted_amount = (total_gold_charges * 10)/100

        elif net_amount >= 300000 and net_amount < 400000:
            discount_in_percentage = 20    
            print('between 3lkh and 4lkh')    
            discounted_amount = (total_gold_charges * 20)/100

        elif net_amount >= 400000 and net_amount < 500000:
            discount_in_percentage = 25
            print('between 4lkh and 5lkh') 
            discounted_amount = (total_gold_charges * 25)/100

else:
    print('You Are Female')
    if age >= 65:
        if net_amount >= 200000 and net_amount < 300000:
            print('between 2lkh and 3lkh-disc 20%')
            discount_in_percentage = 25
            discounted_amount = (total_gold_charges * 25)/100

        elif net_amount >= 300000 and net_amount < 400000:
            discount_in_percentage = 35
            print('between 3lkh and 4lkh')    
            discounted_amount = (total_gold_charges * 35)/100

        elif net_amount >= 400000 and net_amount < 500000:
            discount_in_percentage = 40
            print('between 4lkh and 5lkh') 
            discounted_amount = (total_gold_charges * 40)/100

    else:        
        if net_amount > 200000 and net_amount < 300000:
            print('between 2lkh and 3lkh')
            discount_in_percentage = 15
            discounted_amount = (total_gold_charges * 15)/100

        elif net_amount >= 300000 and net_amount < 400000:
            print('between 3lkh and 4lkh')    
            discount_in_percentage = 25
            discounted_amount = (total_gold_charges * 25)/100

        elif net_amount >= 400000 and net_amount < 500000:
            print('between 4lkh and 5lkh') 
            discount_in_percentage = 30
            discounted_amount = (total_gold_charges * 30)/100
            


payable_amount = net_amount - discounted_amount            
print('================================================')
print('Invoice')
print(F'Name is {name}')
print(F'Gender is {gender}')
print(F'Age is {age}')
print(F'Total Gold Rate is {total_gold_charges}')
print('------------------------------------------------')
print(F'Making Charges - per gram is {making_charges}')
print(F'Total Making Charges - {total_making_charges}')
print('------------------------------------------------')
print(F'Total Amount - {net_amount}')
print(F'Total Discount is {discount_in_percentage}%')
print('================================================')
print(F'Total Payable Amount =  {payable_amount}')