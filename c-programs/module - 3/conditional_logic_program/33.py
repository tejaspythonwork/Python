# input week number and
# print week day

def week_number_day():
    week_day = {
        0 : 'Sunday',
        1 : 'Monday',
        2 : 'Tuesday',
        3 : 'Wednesday',
        4 : 'Thursday',
        5 : 'Friday',
        6 : 'SaturDay'
    }

    choice_of_week_day = int(input('Enter week day - number'))


    if choice_of_week_day in week_day:
          return week_day[choice_of_week_day],choice_of_week_day
    else: 
          return None,choice_of_week_day
    
    
choice,weekday = week_number_day()
if choice is not None:
     print(f'you have entered {choice} and corresponding days = {weekday}')
else:
     print(f'please enter valid number - not valid - {weekday}')