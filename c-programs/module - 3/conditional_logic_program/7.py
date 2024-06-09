# accept marks from user and check pass/fail


def marks_function():
    total_marks = int(input('Please enter your marks'))
    if total_marks <= 39:
        print('Fail')
    else:
        print('Pass')    



marks_function()        