# 06-06-2024
# Guessing Game with 3 level and 2 lifeline

import random 

total_life_line = 2

def level1():
    global total_life_line
    status = True
    computer_guess = random.randint(1, 100)
    chance_level1 = 5
    lower_chances = 0
    upper_chances = 0
    lifeline_use = False
    
    print(computer_guess)

    while status:
        total_chances = lower_chances + upper_chances  # Initialize here
        if total_chances == chance_level1 - 2:
            print('Only 2 Chances Left do you want to use life line enter True or False')
            lifeline_use = input('enter either true/false')
            if(lifeline_use == 'true' and total_life_line!=0):
                #lower_bound = computer_guess - 3
                #upper_bound = computer_guess + 3
                total_life_line = total_life_line -1 
                print(f'Lifeline = {computer_guess}')
                # print(f'{lower_bound} - {upper_bound}')
            else:
                print('Only 2 Chances Left')    
        
        if total_chances >= chance_level1:
            status = False
            print('Total Chances Reached At 5')
            break

        user_guess = int(input('Enter Your Guess (1-100): '))

        if user_guess > computer_guess:
            print('HINT - Guess Lower')
            lower_chances += 1
        elif user_guess < computer_guess:
            print('HINT - Guess Higher')
            upper_chances += 1
        else:
            print('Right Guess')
            print('=================')
            status = False
            level1_won = True
            print('You Have Successfully Completed Level - 1')
            level2()
            print('=================')



def level2():
    global total_life_line
    status_2 = True
    computer_guess_2 = random.randint(1, 150)
    chance_level2 = 8
    lower_chances_2 = 0
    upper_chances_2 = 0
    lifeline_use2 = False
    print(computer_guess_2)
    while status_2:
        total_chances = lower_chances_2 + upper_chances_2  # Initialize here
        if total_chances == chance_level2 - 2:
            print('Only 2 Chances Left do you want to use life line enter True or False')
            lifeline_use = input('enter either true/false')
            if(lifeline_use == 'true' and total_life_line!=0):
                total_life_line = total_life_line -1    
                print(f'Lifeline answer - {computer_guess_2}')
                
                if total_life_line == 0:
                    print('You dont have lifeline remaining') 
                    # print(f'Lifeline = {computer_guess_2}')
                else:
                    print(f'Lifeline = {computer_guess_2}')
                # print(f'{lower_bound} - {upper_bound}')
            else:
                print('Only 2 Chances Left')    
        
        if total_chances >= chance_level2:
            status = False
            print('Total Chances Reached At 8')
            break

        user_guess_2 = int(input('Enter Your Guess (1-150): '))

        if user_guess_2 > computer_guess_2:
            print('HINT - Guess Lower')
            lower_chances_2 += 1
        elif user_guess_2 < computer_guess_2:
            print('HINT - Guess Higher')
            upper_chances_2 += 1
        else:
            print('Right Guess')
            print('======')
            status_2 = False
            level2_won = True
            print('You Have Successfully Completed Level - 2')
            level3()
            print('======')



def level3():
    global total_life_line
    status_3 = True
    computer_guess_3 = random.randint(1, 200)
    chance_level3 = 12
    lower_chances_3 = 0
    upper_chances_3 = 0
    lifeline_use3 = False
    print(computer_guess_3)
    while status_3:
        total_chances = lower_chances_3 + upper_chances_3  # Initialize here
        if total_chances == chance_level3 - 2:
            if(lifeline_use3 == 'true' and total_life_line!=0):
                print('Only 2 Chances Left do you want to use life line enter True or False')
                lifeline_use = input('enter either true/false')
            
                total_life_line = total_life_line -1    
                
                
                if total_life_line == 0:
                    print('You dont have lifeline remaining') 
                else:    
                    print(f'Lifeline = {computer_guess_3}')
                # print(f'{lower_bound} - {upper_bound}')
            else:
                print('Only 2 Chances Left')    
        
        if total_chances >= chance_level3:
            status = False
            print('Total Chances Reached At 12')
            break

        user_guess_3 = int(input('Enter Your Guess (1-200): '))

        if user_guess_3 > computer_guess_3:
            print('HINT - Guess Lower')
            lower_chances_3 += 1
        elif user_guess_3 < computer_guess_3:
            print('HINT - Guess Higher')
            upper_chances_3 += 1
        else:
            print('Right Guess')
            status_3 = False
            level3_won = True
            print('You Have Successfully Completed Level - 3')




level1()
# if level1():
#  print('Level 1 is completed')
#  if level2():
#      print('Level 2 is completed')
#      if level3():
#          print('you have completed all levels')