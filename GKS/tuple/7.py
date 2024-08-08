# rowwise element addition of matrix

def defination7():
    matrix = []
    # row_sum = 0     
    row_sums = []

    Row = int(input('Enter number of rows: '))
    Col = int(input('Enter number of columns: '))

    for row in range(Row):
        a = []
        for col in range(Col):
            a.append(int(input('please enter val: ')))
        matrix.append(a)    



    print('you have entered: ')
    for row in range(Row):
        for col in range(Col):
            print(matrix[row][col],end = ' ')
        print()         

    print('row-wise sum: ')
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)
        print(row_sum)
    print(row_sums)

    
defination7()