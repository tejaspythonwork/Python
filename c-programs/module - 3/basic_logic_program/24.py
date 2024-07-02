# accept 5 employee name and salary count average and total salary

emp1 = input('Enter First Employee Name: ')
sal1 = int(input(f'Enter Salary Of {emp1}: '))

emp2 = input('Enter First Employee Name: ')
sal2 = int(input(f'Enter Salary Of {emp2}: '))

emp3 = input('Enter First Employee Name: ')
sal3 = int(input(f'Enter Salary Of {emp3}: '))

emp4 = input('Enter First Employee Name: ')
sal4 = int(input(f'Enter Salary Of {emp4}: '))

emp5 = input('Enter First Employee Name: ')
sal5 = int(input(f'Enter Salary Of {emp5}: '))

total_salary = sal1 + sal2 + sal3 + sal4 + sal5
avg_sal = total_salary/5

print(f'Total Salary = {total_salary}')
print(f'Average Salary = {avg_sal}')