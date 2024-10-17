# squares of even numbers only

def defination30():
    nums = [1, 2, 3, 4, 5, 6]
    res_square = [x**2 for x in nums if x % 2 == 0]
    print(res_square)


defination30()