# fibonnanci using lambda
def defination3():
    fib_list = [0,1]
    count = 10
    any(map(lambda x: fib_list.append(sum(fib_list[-2:])),range(2,count)))

    return fib_list[:count]


print(defination3())