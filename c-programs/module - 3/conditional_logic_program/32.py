# input salary details and 
# calculate gross salary


def calculate_total_salary():

    basic_salary = int(input('Enter basic salary')) 
    if basic_salary >=0 and basic_salary <=10000:
         hra = (20 * basic_salary )/100
         da = (80 * basic_salary)/100

         total_salary = basic_salary + hra + da
         return total_salary
    elif basic_salary >10000 and basic_salary <=20000:
         hra = (25 * basic_salary )/100
         da = (90 * basic_salary)/100

         total_salary = basic_salary + hra + da    
         return total_salary
    else:
         hra = (30 * basic_salary )/100
         da = (95 * basic_salary)/100

         total_salary = basic_salary + hra + da
         return total_salary
    

net_sal = calculate_total_salary()    
print(f'Your Net Salary = {net_sal}')