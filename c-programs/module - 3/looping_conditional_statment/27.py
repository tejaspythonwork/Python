# series
# 4.
# 1/2 - 2/3 + 3/4 - 4/5 + 5/6 - ...... n 

def defination27(n):
    series_sum = 0
    for i in range(1,n+1):
        term = i / (i + 1)

        if i % 2 == 0:
            series_sum = series_sum - term
        else:
            series_sum = series_sum + term

    return series_sum



n = int(input('Please enter n: '))
res = defination27(n)
print(res.__round__(2))
