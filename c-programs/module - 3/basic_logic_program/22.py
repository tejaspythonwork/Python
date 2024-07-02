# calculate compound interest

'''
amount = P(1 + R/100) * time
compound_interest = amount - p
'''

p = int(input('Enter Principle Amount'))
r = int(input('Enter Rate Of Interest'))
time = int(input('Enter Time In Years')) 

amount = (p * (1 + r/100)) * time
compound_interest = amount - p

print(f'Amount = {amount}')
print(f'Compound Interest = {compound_interest}')