# to check year is leap year or not

year = int(input('Please enter year: '))

if year % 400 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not a leap year')    