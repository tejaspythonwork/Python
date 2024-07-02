# check that given number present in given range
def def49():
    start = int(input('enter start range: '))
    end = int(input('enter end range: '))
    check_number = int(input('enter number to check between range'))

    if start < check_number < end:
        print(f'you entered number {check_number} is between {start} and {end}')
    else:
        print(f'Not in range')    


def49()