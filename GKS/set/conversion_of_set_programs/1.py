# conversion set into tuple and tuple into set
# when we convert set to tuple it convert set values 
# based on internal order of set which is unordered
# therefore element of tuple may not appear same way 
# as they were inserted





def defination1(s):
    print(f'set = {s} type = {type(s)}')

    s_converted = tuple(s)
    print(f'Data Has Been Converted')
    print(f'tuple = {s_converted} and type = {type(s_converted)} ')



input_data = {'a', 'b', 'c', 'd', 'e'}
res = defination1(input_data)