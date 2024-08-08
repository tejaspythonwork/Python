# function to combine n arrays

def defination1(input):
    res = set(input[0])
    for arr in input[1:]:
        res.update(arr)

    return list(res)




input = [[1, 2, 2, 4, 3, 6],
            [5, 1, 3, 4],
            [9, 5, 7, 1],
            [2, 4, 1, 3],
            [11,12,13,14,15,],
            ]

print(defination1(input))