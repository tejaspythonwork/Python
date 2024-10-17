# calculate aggregated dictionaries

def defination90():
    dict1 = {}
    total_wins = 0
    total_losses = 0
    data = {'team1': {'wins': 10, 'losses': 5}, 'team2': {'wins': 12, 'losses': 4}}
    for k in data.values():
        total_wins = k['wins'] + total_wins
        total_losses = k['losses'] + total_losses


    print(f'Total wins = {total_wins}')
    print(f'Total looses = {total_losses}')

defination90()        