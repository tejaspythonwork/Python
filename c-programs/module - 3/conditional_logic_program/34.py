# accept month number and display month name

def display_month_name():
    month_number = int(input('Enter Month Number'))

    match month_number:
        case 1:
            return 'January'
        case 2:
            return 'February'
        case 3:
            return 'March'
        case 4:
            return 'April'
        case 5:
            return 'May'
        case 6:
            return 'June'
        case 7:
            return 'July'
        case 8:
            return 'August'
        case 9:
            return 'September'
        case 10:
            return 'October'
        case 11:
            return 'November'
        case 12:
            return 'December'
        case default:
            return 'Please enter valid month'
        
month_name = display_month_name()

print(month_name)