# list of squres between 1 to 30
# only display first 5 and last 5 squares between 1 to 30

squares = [x*x for x in range(1,31)]
first_five = squares[:5]
last_five = squares[-5:]

print(f'First 5 Elements Whose Square = {first_five}')
print(f'Last 5 Elements Whose Square = {last_five}')