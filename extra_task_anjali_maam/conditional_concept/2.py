# fitness tracker

def defination2():
    duration = int(input('Number of minutes they exercise per week:  '))
    fitness_type = ''
    if duration > 0 and duration < 60:
        fitness_type = 'Sedentary'
    elif duration >= 60 and duration <= 149:
        fitness_type = 'Moderately Active'
    elif duration >= 150 and duration <=299:
        fitness_type = 'Active'
    elif duration >=300:
        fitness_type = 'Very Active'        

    print(f'Your fitness type = {fitness_type}') 


defination2()