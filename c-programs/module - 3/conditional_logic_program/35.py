# read month number and display 
# number of days for this month

def get_days_of_months():

    days_of_months = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
    }

    month = int(input('Enter Month - 1 to 12'))
    if month in days_of_months:
        return days_of_months[month],month
    else:
        return None, month
    
days,month_name = get_days_of_months()

if days is not None:
    print(f'you have entered month is {month_name} and days are {days}')   
else:
    print(f'please enter valid month {month_name} - not valid')    

 