# how to pick random item from range

import random

start_range = int(input('Enter Start Range'))
end_range = int(input('Enter End Range'))

random_number = random.randint(start_range,end_range)
print(f' random number between {start_range} and {end_range} is --- {random_number}')
