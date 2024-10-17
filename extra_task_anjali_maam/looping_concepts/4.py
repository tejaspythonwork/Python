# fizz buzz problem


def defination4():
    for i in range(1,51):
        
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i} = FizzBuzz ')
        elif i % 3 == 0:
            print(f'{i} = Fizz,----',end = ' ')
        elif i % 5 == 0:
            print(f'{i} = Buzz,',end = ' ')
        else:
            print(f' --{i}-- ',end=' ')
defination4()