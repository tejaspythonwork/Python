# convert years into days and days into years
years = int(input('Enter number of years'))
days = int(input('Enter number of days'))

converted_into_years = days/365
converted_into_days = years * 365


print(f'you have entered days = {days} and after conversion years = {converted_into_years.__round__(1)}')
print(f'you have entered years = {years} and after conversion days = {converted_into_days}')