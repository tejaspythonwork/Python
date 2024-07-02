# monday to sunday using switch case 
# consonent or vowel using switch case

# 1.

def day_according_input():
    int_input = int(input('Please enter week-day number'))    
    match int_input:
        case 0:
            return 'sunday'
        case 1:
            return 'monday'
        case 2:
            return 'tuesday'
        case 3:
            return 'wednesday'
        case 4:
            return 'thursday'
        case 5:
            return 'friday'
        case 6:
            return 'saturday'
        case default:
            return 'Please enter valid input between 0-6'

week_day_string = day_according_input()
print(week_day_string)


