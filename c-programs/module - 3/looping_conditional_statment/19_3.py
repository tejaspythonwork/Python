# dimond pattern

def dimond_patterns(n):
    for row in range(1,n,2):
        for space in range(n-row):
           print(' ',end= '')
        for k in range(row):       
           print('* ',end='')   
        print()    

res = dimond_patterns(10)    