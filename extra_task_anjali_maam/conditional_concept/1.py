# determine price of movie tickets based on 
# user's age and day of week

def defination1():
    # for age
    status = True
    base_price = 0
    while status:
        menu = '''
                Please select age
      -------------------------------------------     
           1.childeren (age between 0 - 12)
           2.teenagers (age between 13 - 17) 
           3.adults (age between 18-64)
           4.seniors (age 65 and above)  
           5.for exit - 

               '''  
        print(menu)
        # age = int(input('Enter your age: '))
        choice = int(input('Enter your choice: ')) 
        
        match(choice):
            case 1:
                print('you are children')   
                print('you are eligible for 1 ticket for $5')

                base_price = 5
                discount_based_day_of_week(base_price)
            case 2:
                print('you are teenagers')
                print('you are eligible for 1 ticket for $8')
                base_price = 8
                discount_based_day_of_week(base_price)
            case 3:
                print('you are adults') 
                print('you are eligible for 1 ticket for $12')
                base_price = 12 
                discount_based_day_of_week(base_price)
            case 4:
                print('you are seniors')           
                print('you are eligible for 1 ticket for $7')
                base_price = 7
                discount_based_day_of_week(base_price)
            case 5:
                status = False    

            

def discount_based_day_of_week(base_price):
    status_week = True
    get_discount_percentage = 0
    price = 0
    discounted_price = 0.0
    menu = '''
        please select day 
    =================================
        1. weekend (Saturday or Sunday)
        2. weekday (Monday to friday)
        3. exit
           '''
    while status_week:
        print(menu)
        choice_day = int(input('Please select day: '))
        match(choice_day):
            case 1:
                print('weekend')
                get_discount_percentage = 10
                # print(f'your age = {}')
                print(f'You are on weekend so get discount = {get_discount_percentage}')
                print(f'Base Price =  ${base_price}')
                dis_price = (base_price * 10)/100
                discounted_price = base_price - dis_price   
                print(f'Discounted  = ${dis_price}')             
                print(f'Final Price = ${discounted_price}')
            case 2:
                print('monday to friday')   
                get_discount_percentage = 0 
                print(f'No discount = {get_discount_percentage}')
                print(f'you have to pay = ${base_price} for 1 ticket ')
            case 3:
                status_week = False







defination1()    