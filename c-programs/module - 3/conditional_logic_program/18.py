# program to find profit and loss on given transaction

net_amount = int(input('please enter amount'))
expensis = int(input('please enter expensis in rupees'))

def calProfitAndLoss():
    if net_amount != expensis:
        if net_amount < expensis:
            return 'Loss'
        else:
            return 'Profit'
    else:
        return 'No profit or No loss'    


calc = calProfitAndLoss()
print(calc)