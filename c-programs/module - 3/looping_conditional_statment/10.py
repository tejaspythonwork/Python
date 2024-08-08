# summation of first and last digit
number = 12345

list_of_number = [int(n) for n in str(number)]
print(list_of_number)
summation = list_of_number[0] + list_of_number[-1]
print(f'sum of 1st and last digit = {summation}')