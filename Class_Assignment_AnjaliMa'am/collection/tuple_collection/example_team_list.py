import random
game_status = True
loss_team = ''

while game_status:
    team_list = ['GT','MI','KKR','CSK','RCB','KXIP']
    print('Ipl Teams')
    for i in team_list:
        print(i,end=',')
    print()

    my_team = input('Enter Your Team').upper()
    # print(f'My team = {my_team}')

    team_list.remove(my_team)

    Opp_Team = random.choice(team_list)
    print(f'My Team = {my_team}')
    print(f'Opposite Team = {Opp_Team}')

    # ================================================
    toss_choice = ['H','T']
    print() 
    mytosschoice = input('Enter your toss choice H/T ').upper()
    actual_toss = random.choice(toss_choice)
    print('-------------------------------')
    print(f'Actual Toss = {actual_toss}')
    print('-------------------------------')
    bat_ball_choice = ['BAT','BALL']

    if mytosschoice == actual_toss:
        print(f'{my_team} You won the tosss')
        won_team_choice = input('what do you want - BAT/BALL')
        print(f'you have selected {won_team_choice}')
        won_toss_team = my_team
        loss_team = Opp_Team
    else:
        print(f'You team {my_team} loss the chance')
        opposite_choice = random.choice(bat_ball_choice)
        print(f'Opposite team selected {opposite_choice}')
        loss_team = my_team
        won_toss_team = Opp_Team


    print('------------------Details--------------------')
    print(f'first team = {my_team}')
    print(f'opposite team = {Opp_Team}')
    print(f'Team - Win the toss = {won_toss_team} ')    
    print(f'Team - Loss the toss = {loss_team}')
    # print(f'Team - won the toss = {won_toss_team} ')    

    my_choice = input('Do you want to play again: ')
    if my_choice == 'y' or my_choice == 'yes':
        game_status = True
    else:
        game_status = False    