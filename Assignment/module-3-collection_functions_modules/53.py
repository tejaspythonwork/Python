# pick random value from list or tuple
import random

random_list_1 = ['abc','def','ghi','jkl','mno']
st1 = random.choice(random_list_1)
print(f'Random Choice From list = {st1}')
random_tuple_1 = ((1,2,3),134,('a','b','c'),55.5,121,'q','wqrqer')
st2 = random.choice(random_tuple_1)
print(f'Random Choice From Tuple = {st2}')

