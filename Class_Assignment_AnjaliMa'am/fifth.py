# date - 30-05-2024
# 1. accept years from user and convert it into number of days/months 
# combination of 2 programs

years = int(input('Enter Year: '))
number_of_months = years * 12
number_of_days = years * 365
print(F'Total Months = {number_of_months}')
print(F'Total Days = {number_of_days}')